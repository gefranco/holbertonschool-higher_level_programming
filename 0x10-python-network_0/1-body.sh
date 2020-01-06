#!/bin/bash
# script that displays the size of the body of the response
curl -i -s $1 | grep  Location | sed 's/Location: //' |  sed 's/\r//' | xargs curl
