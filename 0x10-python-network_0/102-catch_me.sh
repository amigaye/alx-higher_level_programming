#!/bin/bash
# Script that causes specific response
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "You got me!"
