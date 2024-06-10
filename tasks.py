from celery import Celery

from model import EmotionClassifier

celery_app = Celery('tasks', backend='redis://redis', broker='pyamqp://guest:guest@rabbitmq')

@celery_app.task(name='analyze_sentiment')
def analyze_sentiment(text):
    sentiment = EmotionClassifier.predict_emotion(text)
    return sentiment