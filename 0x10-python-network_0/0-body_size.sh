#!/bin/bash
# sned url to bash script
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
