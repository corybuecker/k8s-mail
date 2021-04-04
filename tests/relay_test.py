from smtplib import SMTP, SMTPRecipientsRefused
import sys

conn = SMTP(host='localhost', port=10025)

try:
    conn.sendmail('me@example.com', 'email@corybuecker.com', 'test')
except SMTPRecipientsRefused as inst:
    print(inst)
    if inst.args[0] != {'email@example.org': (454, b'4.7.1 <email@example.org>: Relay access denied')}:
        print("it looks like this server accepts relay mail, scary!")
        sys.exit(1)

print(conn)
