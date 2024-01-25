#!/bin/bash
# A script that takes a URLS, send GET request and displays it
curl -sX GET $1 -L
