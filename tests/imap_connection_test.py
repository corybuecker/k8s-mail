from imaplib import IMAP4, IMAP4_SSL
import ssl
import sys

try:
    conn = IMAP4('localhost', 993, timeout=3)
except Exception as inst:
    if inst.args[0] != 'timed out':
        print("it looks like a non-SSL connection was made on port 993")
        sys.exit(1)

try:
    conn = IMAP4('localhost', 143, timeout=3)
except Exception as inst:
    if (inst.args[0] != 'timed out') & (inst.args[0] != 'socket error: EOF'):
        print("it looks like a non-SSL connection was made on port 143")
        sys.exit(1)

context = ssl.SSLContext()
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

conn = IMAP4_SSL('localhost', ssl_context=context)
conn.login('me@k8s-mail.com', 'password')
print(conn.list())
