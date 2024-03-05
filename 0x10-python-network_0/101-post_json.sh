#!/bin/bash
# Script that sends a JSON POST
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
