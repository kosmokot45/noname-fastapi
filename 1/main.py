from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def app_hello():
    return "Hello"