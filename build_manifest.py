import os
import base64
import yaml
import secrets
import string

from argon2 import PasswordHasher

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(64))
ph = PasswordHasher()
hash = ph.hash(password)

with open('volumes/secrets/dovecot_password_file', mode='w+') as dovecot_password_file:
    dovecot_password_file.write(
        f"me@k8s-mail.com:{{ARGON2ID}}{hash}:nobody:nogroup")

print('the one-time password is:')
print(password)
print('this cannot be retrieved again')

sendgrid_token = input("Enter your Sendgrid token: ")

with open('volumes/secrets/dovecot_submission_password_file', mode='w+') as dovecot_submission_password_file:
    dovecot_submission_password_file.write(sendgrid_token or 'bogustoken')


secret = {
    'apiVersion': 'v1',
    'kind': 'Secret',
    'metadata': {
        'name': 'k8s-mail-secrets',
        'namespace': 'k8s-mail',
    },
    'data': {}
}


for file in os.scandir('volumes/secrets'):
    b64 = base64.b64encode(
        bytes(open(file, mode='r').read().rstrip(), 'utf-8'))

    secret['data'][file.name] = b64.decode('utf-8')

output = list(yaml.load_all(
    open('kubernetes.yml', mode='r'), Loader=yaml.FullLoader))


with open('kubernetes_with_secrets.yml', mode='w+') as kubernetes_with_secrets:
    kubernetes_with_secrets.write(yaml.dump_all(output + [secret]).rstrip())
