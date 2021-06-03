import string
import secrets
import os
from argon2 import PasswordHasher

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(64))

if "PASSWORD" in os.environ:
    password = os.environ["PASSWORD"]

ph = PasswordHasher()
hash = ph.hash(password)

with open('volumes/dovecot_password_file', mode='w+') as dovecot_password_file:
    dovecot_password_file.write(
        f"me@k8s-mail.com:{{ARGON2ID}}{hash}:nobody:nogroup")

print('the one-time password is:')
print(password)
print('this cannot be retrieved again')

sendgrid_token = input("Enter your Sendgrid token: ")

with open('volumes/dovecot_submission_password_file', mode='w+') as dovecot_submission_password_file:
    dovecot_submission_password_file.write(sendgrid_token or 'bogustoken')
