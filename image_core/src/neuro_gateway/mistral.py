import requests

from pydantic import BaseModel

from commons.neuro_gateway.api import API

URL = 'https://ai.rt.ru/api/1.0/mistral/chat_universal'

headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': None,
    'Content-Type': 'application/json',
}

data = {
    'chat': {
        'user_messange': None,
        'temperature': 0.9,
        'system_prompt': 'Ты менеджер рекламного агентства, придумываешь креативную рекламу',
        'messages': [],
        'chat_history': []
    }
}

class Mistral(API):
    """
    """
    def send_message(self, message: str) -> str:
        """
        """
        data['chat']['user_messange'] = message
        return self.send_post(URL, data)[0]['message']['content']