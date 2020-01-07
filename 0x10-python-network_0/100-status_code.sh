#!/bin/bash
# script that displays the size of the body of the response
curl -s -i -w "%{http_code}" $1 -o /dev/null
