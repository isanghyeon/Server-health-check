#!/bin/sh


#docker container id check
echo "=> docker container ID"

id="$(docker ps -aq)"
echo "$id"

all_num=$(echo "$id" | wc '-w')

echo "========================================"

SET=$(seq 1 $allnum)

for num in $SET
do
        line=$(echo "$id" | sed '-n' "$num"'p')

        #docker stop
        echo "=> docker $line container stop"
        docker stop $line

        #docker export container(file name: time.tar)
        echo "=> docker $line container export"
        docker export $line > /var/backups/ServerBackups/"$line""$(date "+%Y%m%d").tar"

        #docker start
        echo "=> docker $line container restart"
        docker restart $line
        echo "========================================" 
done
docker exec $LOGOS_WEB_SERVER_CID service apache2 restart
