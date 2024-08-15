path=$1
tracker=$2

docker rm l4g-upload-assistant

docker run \
  -d \
  --name='l4g-upload-assistant' \
  --network=htpc \
  -v '/share_media':'/downloads':'rw' \
  -v '/appdata/l4g-upload-assistant/config.py':'/Upload-Assistant/data/config.py':'rw' \
  -v '/appdata/qbittorrent-private/qBittorrent/BT_backup/':'/BT_backup':'rw' \
  -v '/appdata/l4g-upload-assistant/tmp':'/Upload-Assistant/tmp':'rw' 'ghcr.io/l4gsp1ke/upload-assistant:master' \
  "/downloads/torrents/$path" \
  --unattended \
  --trackers $tracker

docker logs -f l4g-upload-assistant
