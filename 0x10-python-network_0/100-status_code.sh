#!/bin/bash
# script that displays the size of the body of the response
curl -i -s $1 | head -n 1 | cut  -d " " -f 2
