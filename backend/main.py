from fastapi import FastAPI

app = FastAPI(
    title="DJOS API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DJOS"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "DJOS API",
        "version": "0.1.0"
    }