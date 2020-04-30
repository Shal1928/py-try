#!/bin/bash
#Для подключения к серверу через ssh укажите адрес первым в передаваемых аргументах
EARS_PATH="/workdir/devops-scripts/autoDeploy/ears"
WS_PROFILES="/opt/IBM/WebSphere/AppServer/profiles"
U="user"
P="password"
INVOKE="AdminControl.invoke"
TOKEN="X-Auth-Token: $3"
U_ID="X-User-Id: $4"
JSON="Content-type:application/json"
CHANNEL=""
MESSAGE="1"

appManager () {
#stop
#start
    NODE_NAME="node01"
    APP_SRV_NAME="$1_cluster_$NODE_NAME"
    APP_MANAGER="AdminControl.queryNames('name=ApplicationManager,process=$APP_SRV_NAME,*')"
    echo "-user $U -password $P -c \"$INVOKE($APP_MANAGER,'$2Application','$3')\" -lang jython"
}

nodeManager () {
    echo "-user $U -password $P -c \"$INVOKE(AdminControl.completeObjectName('type=NodeSync,process=nodeagent,node=node0$1,*'),'sync')\" -lang jython"
}

if [ "$2" == "integration" ]; then
    CURRENT_VERSION=$(mvn help:evaluate -Dexpression=project.version -q -DforceStdout)
	BASE_URL=""
    INTEGRATION_PART="ear/$CURRENT_VERSION/ear-$CURRENT_VERSION.ear"
    ACCOUNTING_STUB_PART="accounting-stub/$CURRENT_VERSION/accounting-stub-$CURRENT_VERSION.war"
    NSI_STUB_PART="nsi-stub/$CURRENT_VERSION/nsi-stub-$CURRENT_VERSION.war"
    common_CONFIG="common-$CURRENT_VERSION.zip"
    CONFIG_PART="common/$CURRENT_VERSION/$common_CONFIG"
    CFG_PATH=""
    ssh -tt root@$1 << EOFSSH
        TODAY=`date '+%Y-%m-%d___%H:%M:%S'`
        cd "$EARS_PATH"
        wget -O "$common_CONFIG" "$BASE_URL/$CONFIG_PART"
        unzip "$common_CONFIG" -d "" && rm -f "$common_CONFIG" && zip -r "___\${TODAY}.zip" "$CFG_PATH"* && rm -r -f "$CFG_PATH"*
        rsync -av --remove-source-files "config-$CURRENT_VERSION/"* "$CFG_PATH" && rm -r -f "config-$CURRENT_VERSION"
        wget -O "01-app-integration-$CURRENT_VERSION.ear" "$BASE_URL/$INTEGRATION_PART"
        wget -O "10-accounting-stub-$CURRENT_VERSION.war" "$BASE_URL/$ACCOUNTING_STUB_PART"
        #nsi-stub размещается сразу /DONE и устанавливается только при запуске autoDeploy2.sh
        wget -O "./DONE/11-nsi-stub-$CURRENT_VERSION.war" "$BASE_URL/$NSI_STUB_PART"
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager "" stop app-common)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager 2 stop app2-common)
        /workdir/devops-scripts/autoDeploy/autoDeploy/autoDeploy.sh
        /workdir/devops-scripts/autoDeploy/autoDeploy/autoDeploy2.sh
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(nodeManager 1)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(nodeManager 2)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager "" start app-common)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager "" start app-integration)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager "" start app-test-accounting-stub)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager "" start nsi-stub)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager 2 start app2-common)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager 2 start app2-integration)
        /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $(appManager 2 start app2-test-accounting-stub)
        exit
EOFSSH
    MESSAGE="The following applications have been updated: to version $CURRENT_VERSION"
fi

if [ "$2" == "common" ]; then
    CURRENT_VERSION=$(mvn help:evaluate -Dexpression=common.version -q -DforceStdout)
	BASE_URL=""
    common_PART="ear/$CURRENT_VERSION/ear-$CURRENT_VERSION.ear"
    TRANSFORMER_PART="transformer/$CURRENT_VERSION/transformer-$CURRENT_VERSION.war"
    ssh -tt root@$1 <<EOFSSH
        cd "$EARS_PATH"
        wget -O "02-common-$CURRENT_VERSION.ear" "$BASE_URL/$common_PART"
        wget -O "06-transformer-$CURRENT_VERSION.war" "$BASE_URL/$TRANSFORMER_PART"
        exit
EOFSSH
fi

if [ "$2" == "gate" ]; then
    GATE_VERSION=$(mvn help:evaluate -Dexpression=gate.version -q -DforceStdout)
	BASE_URL=""
    GATE_PART="gate-war/$GATE_VERSION/gate-war-$GATE_VERSION.war"
    EDB_VERSION=$(mvn help:evaluate -Dexpression=lbedb.version -q -DforceStdout)
    EDB_BASE_URL=""
    EDB_PART="lbedb/$EDB_VERSION/lbedb-$EDB_VERSION.war"
    ssh -tt root@$1 <<EOFSSH
        cd "$EARS_PATH"
        wget -O "03-gate-$GATE_VERSION.war" "$BASE_URL/$GATE_PART"
        wget -O "05-lbedb-$EDB_VERSION.war" "$EDB_BASE_URL/$EDB_PART"
        exit
EOFSSH
fi

if [ "$2" == "dss" ]; then
    CURRENT_VERSION=$(mvn help:evaluate -Dexpression=dss.service.version -q -DforceStdout)
	BASE_URL=""
    DSS_PART="dss-service-ear/$CURRENT_VERSION/dss-service-ear-$CURRENT_VERSION.ear"
    ssh -tt root@$1 <<EOFSSH
        cd "$EARS_PATH"
        wget -O "04-dss-service-$CURRENT_VERSION.ear" "$BASE_URL/$DSS_PART"
        exit
EOFSSH
fi

TMID=$(curl -H "$TOKEN" -H "$U_ID" -H "$JSON" https://rchat.*.ru/api/v1/chat.sendMessage -d "{\"message\": { \"rid\": \"$CHANNEL\", \"msg\": \"$MESSAGE\" }}") 2>&1
echo $TMID
#| grep -Po '"_id":.*?[^\\]",'