#!/usr/bin/env python3

import base64
import os
import secrets
import string
import sys
import yaml


secret = {
    'apiVersion': 'v1',
    'kind': 'Secret',
    'metadata': {
        'name': 'k8s-mail-secrets',
        'namespace': 'k8s-mail',
    },
    'data': {}
}


for file in os.scandir('volumes'):
    b64 = base64.b64encode(
        bytes(open(file, mode='r').read().rstrip(), 'utf-8'))

    secret['data'][file.name] = b64.decode('utf-8')

output = list(yaml.load_all(
    open('kubernetes.yml', mode='r'), Loader=yaml.FullLoader))


with open('kubernetes_with_secrets.yml', mode='w+') as kubernetes_with_secrets:
    kubernetes_with_secrets.write(yaml.dump_all(output + [secret]).rstrip())
