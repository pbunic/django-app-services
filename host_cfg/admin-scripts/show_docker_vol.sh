#!/bin/sh

# Show docker volumes and corresponding container mounts

volumes=$(docker volume ls  --format '{{.Name}}')

for volume in $volumes; do
  echo && echo $volume
  docker ps -a --filter volume="$volume"  --format '{{.Names}}' | sed 's/^/└──/'
done
echo
