from smtplib import SMTP, SMTP_SSL
import ssl
import sys

try:
    conn = SMTP(host='mail.k8s-mail.com', port=587)
    conn.sendmail('me@k8s-mail.com', 'email@example.org', 'test')
except Exception as e:
    if e.args != (530, b'5.7.0 TLS required.', 'me@k8s-mail.com'):
        print('woah, the submission accepts non-TLS')
        sys.exit(1)

try:
    conn = SMTP(host='mail.k8s-mail.com', port=587)
    conn.login('bad', 'password')
except Exception as e:
    if e.args != ('SMTP AUTH extension not supported by server.',):
        print('woah, the submission accepts non-TLS authentication')
        sys.exit(1)

try:
    conn = SMTP(host='mail.k8s-mail.com', port=587)
    conn.starttls()
    conn.login('bad', 'password')
except Exception as e:
    if e.args != (535, b'5.7.8 Authentication failed.'):
        print('woah, the submission accepts bad authentication')
        sys.exit(1)

conn = SMTP(host='mail.k8s-mail.com', port=587)
conn.starttls()
conn.login('me@k8s-mail.com', 'password')


conn.sendmail('me@k8s-mail.com', 'me@example.org',
              'From: me@k8s-mail.com\nTo: me@example.org')
