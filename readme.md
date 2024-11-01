# instalar gestor de paquetes primero
# python3 -m pip install uv
# pip install uv 

# Crea la carpeta con el virtualenv (.venv)
# uv venv 

# Toma el requirements y calcula las dependencias transitivas hacia el requirements.txt
# python -m uv pip compile requirements.in --output-file requirements.txt

# instala todas las dependencias
# python -m uv pip sync requirements.txt

# select interpreter en vscode
# Ejecutar normalmente en modo run o debug

