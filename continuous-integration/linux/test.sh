#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR=$(realpath "$SCRIPT_DIR/../..")

source $SCRIPT_DIR/venv.sh || exit $?
activate_venv || exit $?

python3 -m pip install --requirement "$SCRIPT_DIR/../python-requirements/test.txt" || exit $?

python -m pytest "$ROOT_DIR" -c "$ROOT_DIR/pytest.ini" || exit $?

echo Success! ["$0"]
