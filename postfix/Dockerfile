FROM alpine:3

RUN apk --no-cache add postfix openssl bash

COPY startup.sh /usr/bin/startup.sh
COPY main.cf /etc/postfix/main.cf
COPY virtual /etc/postfix/virtual

CMD ["startup.sh"]
