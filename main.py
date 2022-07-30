from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Prasad"}


@app.get("/add/str1")
async def add(str1):
    en = str1
    return {"Entered Value": en}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
