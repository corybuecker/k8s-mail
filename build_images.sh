#!/bin/bash

set -ex

docker buildx build -t corybuecker/k8s-mail:postfix --platform linux/amd64,linux/arm64/v8 --push ./postfix
docker buildx build -t corybuecker/k8s-mail:dovecot --platform linux/amd64,linux/arm64/v8 --push ./dovecot

docker compose build
