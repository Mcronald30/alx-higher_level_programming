#!/bin/bash
# script that takes, and sends a request URL, and displays the size
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
