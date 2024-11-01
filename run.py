import uvicorn
from src.app import app
from src.config import API_PORT, API_HOST

if __name__ == '__main__':
    uvicorn.run(app, host=API_HOST, port=API_PORT, log_level="debug")


# Extensiones
# indent-rainbow
# Trailing Spaces (ctrl +k +x elimina todos los trailing spaces)
