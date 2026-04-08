from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict, is_korean_spam

app = FastAPI(title="Spam Classifier API", version="1.0.0")

class MessageRequest(BaseModel):
    text: str

class MessageResponse(BaseModel):
    text: str
    prediction: str
    is_korean_spam: bool

@app.get("/")
def read_root():
    return {"message": "Spam Classifier API is running!"}

@app.post("/predict", response_model=MessageResponse)
def predict_spam(request: MessageRequest):
    pred = predict(request.text)
    is_kr_spam = is_korean_spam(request.text)
    return MessageResponse(text=request.text, prediction=pred, is_korean_spam=is_kr_spam)
