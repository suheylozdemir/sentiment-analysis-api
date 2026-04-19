from fastapi import FastAPI
from transformers import pipeline
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

classifier = pipeline("sentiment-analysis")

Instrumentator().instrument(app).expose(app)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(text: str):
    result = classifier(text)
    return {"text": text, "result": result}