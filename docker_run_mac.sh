#!/bin/bash
printf "\n[+] (Mac) Running Docker Container"
docker run --rm -it -v "$PWD:/root" devi
