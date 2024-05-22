from fastapi import FastAPI

app = FastAPI()


@app.get("/auth")
def get_user():
    return {"user": "authenticated"}
