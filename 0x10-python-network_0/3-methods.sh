#!/bin/bash
# script that displays the size of the body of the response
curl -s -i $1 | grep Allow: | sed 's/Allow: //g'
