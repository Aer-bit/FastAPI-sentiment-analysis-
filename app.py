from celery import Celery
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

celery_app = Celery('tasks',
    backend='redis://redis',
    broker='pyamqp://guest:guest@rabbitmq'
)

@app.get('/')
def home():
    return {'Hello! You have accessed ML project API. To see list of available commands add /docs in the url.'}


@app.post("/predict/")
async def predict_emotion(text_request: TextRequest):
    async_result = celery_app.send_task("analyze_sentiment", args=[text_request.text])
    result = async_result.get()
    return result