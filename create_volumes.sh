#!/bin/bash

set -ex

rm -rf volumes
mkdir -p volumes

openssl req \
    -new \
    -newkey rsa:4096 \
    -nodes \
    -keyout volumes/dovecot.key \
    -out volumes/dovecot.cer \
    -subj "/C=US/ST=None/L=None/CN=k8s-mail.com" \
    -days 365 \
    -x509

/usr/bin/env python3 create_volumes.py

chmod 444 volumes/*
