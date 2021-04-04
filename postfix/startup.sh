#!/bin/bash

set -ex

postmap /etc/postfix/virtual
newaliases

postfix start-fg
