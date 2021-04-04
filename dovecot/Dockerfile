FROM alpine:3

RUN apk --no-cache add dovecot dovecot-lmtpd dovecot-submissiond bash

COPY dovecot.conf /etc/dovecot/dovecot.conf
COPY startup.sh /usr/bin/startup.sh

CMD ["startup.sh"]
