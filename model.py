import torch
from transformers import pipeline

torch.set_num_threads(1)
#устанавливаем количество потоков

class EmotionClassifier:
    """
    Классификатор эмоций на основе предобученной модели Transformers.
    """
    model = pipeline(model="seara/rubert-tiny2-ru-go-emotions")

    @classmethod
    def predict_emotion(cls, text: str):
        """
        Предсказание эмоций по тексту.
        Args:
            text (str): Текст для анализа эмоций.
        """
        result = cls.model(text)
        return result