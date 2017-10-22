#!/bin/bash
# to log environmental variables:
env > /app/env_variables.log

setup_ssh() {
  if ($ENABLE_SSH == "true")
  then
      echo "[*] Enabling SSH server"
      cp /app/supervisor/sshserver.conf /etc/supervisor/conf.d/
  else
      echo "[*] SSH server disabled by configuration"
      rm /etc/supervisor/conf.d/sshserver.conf 2> /dev/null
  fi
}

# start ssh service, only if ENABLE_SSH env variable is set to true
setup_ssh

echo "[*] Start supervisor"
supervisord -n