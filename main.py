from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}
@app.get("/hello")
def read_about():
    return {"world":"hello"}

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)