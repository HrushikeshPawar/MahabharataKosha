from fastapi import FastAPI

app = FastAPI(title="Mahabharata Kosha API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Mahabharata Kosha API"}
