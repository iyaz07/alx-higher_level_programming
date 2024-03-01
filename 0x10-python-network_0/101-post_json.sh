#!/bin/bash
#send JSON POST request to URL passed as first arg, display body of response.
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
