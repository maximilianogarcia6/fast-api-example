from fastapi import FastAPI, HTTPException, status
import uvicorn

app = FastAPI()

messages = {"message_0":"Hello, World!"}

@app.post("/message", status_code=status.HTTP_201_CREATED)
def create_message(message: str) -> str:
    current_index = len(messages) + 1
    next_key_index = f"message_{current_index}"
    messages[next_key_index] = message

    return f"Message number {current_index} Created!"

@app.get("/", tags=["users"])
def get_all_messages() -> dict:
    """Descripcion de prueba esta api es para obtener *mensajes*"""
    if not messages:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No message found!")
    
    return messages

@app.get("/message/{id}")
def get_message(id: int) -> str:
    this_key = f"message_{id}"
    if not this_key in messages:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Message number {id} not found!")
    
    return messages[this_key]

@app.put("/message/{id}")
def update_message(id: int, message: str) -> str:
    this_key = f"message_{id}"

    if not this_key in messages:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Message number {id} not found!"
        )
    
    messages.update({this_key: message})
    return f"Message number {id} Updated!"

@app.delete("/message/{id}")
def delete_message(id: int) -> str:
    this_key = f"message_{id}"

    if not this_key in messages:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Message number {id} not found!"
        )
    
    messages.pop(this_key)
    return f"Message number {id} Updated!"

@app.delete("/")
def delete_all() -> str:
    if not messages:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No message found!")

    messages.clear()
    return "All the messages were deleted!"


