#!/bin/sh

# Check if a command-line argument is provided
if [ -n "$1" ]; then
	CONNECT_ARG="connect $1"
else
	CONNECT_ARG=""
fi

echo "=====<<<<<Uploading>>>>>=====";
uvx mpremote $CONNECT_ARG fs cp -r boot.py main.py config.json modules :.;
echo "=====<<<<<Done>>>>>=====";
uvx mpremote $CONNECT_ARG fs ls;
uvx mpremote $CONNECT_ARG fs ls modules;
uvx mpremote $CONNECT_ARG reset;
