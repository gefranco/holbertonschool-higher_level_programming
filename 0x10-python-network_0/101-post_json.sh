#!/bin/bash
# script that displays the size of the body of the response
curl -s -d "@$2" -X POST -H "Content-Type: application/json" $1
