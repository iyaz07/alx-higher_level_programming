#!/bin/bash
#request to cause the server to respond with "You got me!",in body of response.
curl -sL 0:5000/catch_me -X PUT "You got me!"
