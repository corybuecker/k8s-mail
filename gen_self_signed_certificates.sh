#!/bin/bash

set -ex

rm -f volumes/secrets/dovecot.key volumes/secrets/dovecot.cer

openssl req \
    -new \
    -newkey rsa:4096 \
    -nodes \
    -keyout volumes/secrets/dovecot.key \
    -out volumes/secrets/dovecot.cer \
    -subj "/C=US/ST=None/L=None/CN=k8s-mail.com" \
    -days 365 \
    -x509

chmod 400 volumes/secrets/dovecot.{key,cer}
