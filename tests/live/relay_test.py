from smtplib import SMTP, SMTPRecipientsRefused
import sys

# This test works in docker because the connection does not come from localhost,
# but from the Docker host network. Normally, localhost is a trusted sender for
# Postfix.

conn = SMTP(host='mail.k8s-mail.com', port=25)

try:
    conn.sendmail('me@example.org', 'email@example.com', 'test')
except SMTPRecipientsRefused as inst:
    print(inst)
    if inst.args[0] != {'email@example.com': (454, b'4.7.1 <email@example.com>: Relay access denied')}:
        print("it looks like this server accepts relay mail, scary!")
        sys.exit(1)

print(conn)
