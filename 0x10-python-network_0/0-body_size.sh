#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -w '%{size_download}\n' -s -o /dev/null "$1"
