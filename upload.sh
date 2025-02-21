#!/bin/sh
echo "=====<<<<<Uploading>>>>>=====";
uvx mpremote fs cp -r boot.py main.py config.json modules :.;
echo "=====<<<<<Done>>>>>=====";
uvx mpremote fs ls;
uvx mpremote fs ls modules;
uvx mpremote reset;
