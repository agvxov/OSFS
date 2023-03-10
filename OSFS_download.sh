#!/bin/bash

URL="https://www.opensocietyfoundations.org/grants/past?page="
if [ -n "$1" ]; then
	DUMPFILE="$1"
else
	DUMPFILE=dump.log
fi
echo '' > "$DUMPFILE"

I='0'
while true; do
	echo "${URL}${I}:"
	curl "${URL}${I}" | tee --append $DUMPFILE | grep '<li class="m-grantsDatabase__item">' &> /dev/null || break
	I=$(expr $I + 1)
done
