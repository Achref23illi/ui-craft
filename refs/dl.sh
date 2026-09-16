#!/bin/bash
# usage: dl.sh ids-file  — downloads thumbs into screens/<app>/
# ids-file format: one or more "appId:uuidNoDashes,uuidNoDashes,...;" blocks (Refero screenshot ids).
# Requires your own Refero account to collect ids; screens are the app makers' copyrighted UI.
cd "$(dirname "$0")"
tr ';' '\n' < "$1" | while IFS=: read -r app ids; do
  [ -z "$app" ] && continue
  mkdir -p "screens/$app"
  echo "$ids" | tr ',' '\n' | while read -r id; do
    [ -z "$id" ] && continue
    u="${id:0:8}-${id:8:4}-${id:12:4}-${id:16:4}-${id:20:12}"
    f="screens/$app/$u.jpg"
    [ -s "$f" ] || curl -sL -A "Mozilla/5.0" -o "$f" "https://images.refero.design/screenshots/$app/mobile/${u}_thumb.jpg" &
    # keep ~12 parallel
    while [ "$(jobs -rp | wc -l)" -ge 12 ]; do sleep 0.2; done
  done
done
wait
echo "done $(find screens -name '*.jpg' | wc -l) files"
