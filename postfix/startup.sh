#!/bin/bash

set -ex

postmap /etc/postfix/virtual
newaliases

exec postfix start-fg
