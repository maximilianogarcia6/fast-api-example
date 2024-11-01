#!/bin/bash

# Find Python and Pip OS commands:
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    PYTHON_CMD=$(which python3 || which python)
    PIP_CMD=$(which pip3 || which pip)
elif [[ "$OSTYPE" == "darwin"* ]]; then
    PYTHON_CMD=$(which python3 || which python)
    PIP_CMD=$(which pip3 || which pip)
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    PYTHON_CMD=$(where python)
    PIP_CMD=$(where pip)
else
    echo "Sistema operativo no soportado."
    exit 1
fi

echo "Usando $PYTHON_CMD para Python"
echo "Usando $PIP_CMD para Pip"

# Instalar dependencias usando pip y UV
$PIP_CMD install uv
$PYTHON_CMD -m uv venv
$PYTHON_CMD -m uv pip compile requirements.in --output-file requirements.txt
$PYTHON_CMD -m uv pip sync requirements.txt

