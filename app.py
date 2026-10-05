from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "name": "PinContext",
        "message": "Pinterest × AI",
        "status": "Em desenvolvimento"
    }


@app.get("/health")
def health():
    return {"status": "ok"}