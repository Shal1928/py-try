#!/bin/bash
#Полное имя плагина: org.apache.maven.plugins:maven-help-plugin:3.0.0:evaluate
CURRENT_VERSION=$(mvn help:evaluate -Dexpression=project.version -q -DforceStdout)
echo "Add char '-' to end version number for adding 'SNAPSHOT'."
echo -n "Enter the new version to set $CURRENT_VERSION: "
read NEW_VERSION
if [ "${NEW_VERSION: -1}" == "-" ]; then
	NEW_VERSION="${NEW_VERSION}SNAPSHOT"
fi
echo $NEW_VERSION
mvn versions:set -DnewVersion=$NEW_VERSION
mvn versions:commit

echo -n $"Please push [Enter] for commit&push: 'Change version to $NEW_VERSION' or type any char for exit: "
read IS_COMMIT
if [ ! -z "$IS_COMMIT" ]; then
	exit 0
fi
git commit -a -m "Change version to $NEW_VERSION"
git push origin HEAD
