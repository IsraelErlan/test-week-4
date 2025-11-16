from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from utils.caesar_encryption import caeser_encrypt, caeser_decrypt
from utils.fence_encryption import fence_encrypt, fence_decrypt
from utils.stats_manager import save_stats

app = FastAPI()

class Caeser(BaseModel):
    text: str
    offset: int 
    mode: str 

class Fence(BaseModel):
    text: str



@app.get("/test")
def get_test_message():
    save_stats("/test", "GET", 10)
    return {"msg": "hi from test"}



@app.get("/test/{name}")
def save_user(name):
    with open("names.txt", 'a') as f:
        f.write(name + '\n')
    save_stats("/test/:name", "GET", 10)
    return {"msg": "saved user"}



@app.post("/caesar")
def caesar_cipher(budy: Caeser):
    text_result = ""
    mode = budy.mode
    if mode == "encrypt":
        text_result = caeser_encrypt(budy.text, budy.offset)
    elif mode == "decrypt":
        text_result = caeser_decrypt(budy.text, budy.offset)

    save_stats("/caesar", "POST", 10)
    return {mode + "ed": text_result}

@app.get("/fence/encrypt")
def encrypted_by_fence_cipher(text):
    encrypted_text = fence_encrypt(text)
    save_stats("/fence/encrypt", "GET", 10)
    return {"encrypted_text": encrypted_text}

@app.post("/fence/decrypt")
def decrypt_by_fence_cipher(budy: Fence):
    text = budy.text
    decrypted_text = fence_decrypt(text)
    save_stats("/fence/decrypt", "POST", 10)
    return {"decrypted_text": decrypted_text}

if __name__ == '__main__':
    uvicorn.run(app, host = "localhost", port = 8000)