#!/bin/bash

set -ex

check_permissions () {
  if [ ! -f "$1" ]; then
    echo "$1 does not exist"
    exit 1
  fi

  if [ ! $(stat -L -c %a $1) -eq 444 ]; then
    echo "bad permissions on $1...must be 444"
    exit 1
  fi
}

if [[ ! -z "${INITIALIZE_USER}" ]]; then
    echo "initializing"
    echo $INITIALIZE_USER
    mkdir -p /home/$INITIALIZE_USER
    chown -R nobody:nogroup /home/$INITIALIZE_USER
fi

check_permissions "/etc/dovecot/secrets/dovecot_password_file"
check_permissions "/etc/dovecot/secrets/dovecot_submission_password_file"
check_permissions "/etc/dovecot/secrets/dovecot.key"
check_permissions "/etc/dovecot/secrets/dovecot.cer"

# The permissions check out, let's start Dovecot as a foreground process.

# Using exec replaces the PID of this script with the PID of dovecot. This
# allows faster shutdown by docker.

exec dovecot -F
