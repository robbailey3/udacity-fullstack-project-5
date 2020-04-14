#!/bin/sh
# init_venv.sh
if [ -d "./venv/bin" ];then
  echo "[info] Ctrl+d to deactivate"
  bash -c ". ./venv/bin/activate; exec /usr/bin/env bash --rcfile <(echo 'PS1=\"(venv)\${PS1}\"') -i;"
fi
