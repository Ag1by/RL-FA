from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}
@app.get("/hello")
def read_about():
    return {"world":"hello"}