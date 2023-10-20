#!/bin/sh

# Script for incremental docker volumes backup with rsync utility
# !!! not yet finished

if ! [ -f /usr/bin/rsync ]; then
	echo "ERROR: rsync isn't installed on the system."
fi

CURDATE=$(date +%Y-%m-%d)
SRC="/var/lib/docker/volumes/"
BAK="./docker-vol-backup/"
sudo rsync -avb --delete --backup-dir=../docker-vol-incr-backup/$CURDATE $SRC $BAK
sudo chown -R $USER:$USER *