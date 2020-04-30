#!/bin/bash
LINK=$(curl --silent --user $2:$3 -X POST http://$1:8085/rest/api/latest/queue/$4$5.json | jq -r .link.href)
LINK=${LINK%$'\r'}.json?expand=stages.stage.results.result
echo $LINK
echo "Build Started!"
IS_FINISHED=$(curl --silent --user $2:$3 -X GET $LINK | jq -r .finished)
while [ "${IS_FINISHED}" == "$(curl --silent --user $2:$3 -X GET $LINK | jq -r .finished)" ]
do
    IS_FINISHED=$(curl --silent --user $2:$3 -X GET $LINK | jq -r .finished)
    PROGRESS=$(curl --silent --user $2:$3 -X GET $LINK | jq -r '.progress.percentageCompletedPretty + " - " + .progress.prettyTimeRemainingLong')
    echo "Progress: $PROGRESS"
done
IS_SUCCESSFUL=$(curl --silent --user $2:$3 -X GET $LINK | jq -r '.status.stages.stage[] | .isSuccessful')
echo "Build finished is successful: $IS_SUCCESSFUL"