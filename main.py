from fastapi import FastAPI
import uvicorn
from fastapi.responses import PlainTextResponse
from public.pub import user_router

app = FastAPI()

app.include_router(user_router)

@app.get('/')
async def f_indef():
    return {"FName": "Илья","LName":"Зинченко"}


if __name__ == '__main__':
    uvicorn.run(app = "main:app", host="127.0.0.1", port=4800)