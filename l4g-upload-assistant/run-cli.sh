#!/bin/sh
docker rm l4g-upload-assistant-cli

docker run \
  -d \
  --name='l4g-upload-assistant-cli' \
  --network=htpc \
  --entrypoint tail \
  -v '/share_media':'/data':'rw' \
  -v '/appdata/l4g-upload-assistant/config.py':'/Upload-Assistant/data/config.py':'rw' \
  -v '/appdata/qbittorrent/qBittorrent/BT_backup/':'/BT_backup':'rw' \
  -v '/appdata/l4g-upload-assistant/tmp':'/Upload-Assistant/tmp':'rw' 'ghcr.io/audionut/upload-assistant:master' \
  -f /dev/null

docker exec -it l4g-upload-assistant-cli /bin/sh
## After this, you can python3 upload.py --help
## To exit, type exit
