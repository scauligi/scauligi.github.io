#!/usr/bin/env bash
set -eu

function quit() {
  echo "quit" >&2
  exit
}
trap quit INT TERM

fname=INITIAL
while true; do
  printf "%-20s" "$fname"
  sleep 0.5
  date
  ./index.md.py
  fname=$(fswatch -1 --event Updated --latency 0.1 _data/papers.yaml index.md.py | head -n1)
  fname=$(realpath --relative-to=. "$fname")
done

quit
