#!/bin/bash

set -ex

docker build --platform linux/amd64 -t corybuecker/k8s-mail:postfix ./postfix
docker build --platform linux/amd64 -t corybuecker/k8s-mail:dovecot ./dovecot

docker push corybuecker/k8s-mail:postfix
docker push corybuecker/k8s-mail:dovecot

docker compose build
