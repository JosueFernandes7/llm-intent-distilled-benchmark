from enum import Enum

class MistralModel(str, Enum):
    SMALL_LATEST = "mistral-small-latest"
    MEDIUM_LATEST = "mistral-medium-latest"
    LARGE_LATEST = "mistral-large-latest"
