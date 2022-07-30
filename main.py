from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello Prasad"}


@app.get("/test")
def test():
    return {"message": "Test Worked"}


@app.get("/add/str1")
def add(str1):
    en = str1
    return {"Entered Value": en}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
