from fastapi import FastAPI

app = FastAPI(title="rest-api-kube")


@app.get("/")
def read_root() -> dict:
    return {"message": "Hello, World!"}
