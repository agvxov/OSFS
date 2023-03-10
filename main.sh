#!/bin/bash

DUMPFILE="dump.log"

./OSFS_download.sh "$DUMPFILE"
#./OSFS_parser.py "test.txt"
./OSFS_parser.py "$DUMPFILE"
