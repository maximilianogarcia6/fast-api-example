# This project is an example to run a single FastAPI application

## How to create a python environment to run the codes for mock data creation
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pip-tools 
python -m piptools compile requirements.in --output-file requirements.txt
python -m piptools sync requirements.txt
```


