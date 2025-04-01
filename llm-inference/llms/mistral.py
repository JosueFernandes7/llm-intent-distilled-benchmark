from mistralai import Mistral
from core.settings import settings
from mistral_models import MistralModel


class MistralChat:
    def __init__(self):
        self.client = Mistral(api_key=settings.MISTRAL_API_KEY)

    def get_response(
        self, message: str, model: MistralModel = MistralModel.SMALL_LATEST
    ) -> str:
        self.client.chat.complete(
            model=model.value,
            messages=[
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )
