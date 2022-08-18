#!/bin/bash
curl -w '%{size_download}\n' -s -o /dev/null "$1"
