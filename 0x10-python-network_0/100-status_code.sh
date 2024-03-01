#!/bin/bash
#send request to URL passed as argument, displays status code of response.
curl -s "$1" -o /dev/null -w "%{http_code}"
