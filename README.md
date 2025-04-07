https://archive.ics.uci.edu/dataset/570/clinc150

# Rasa API Documentation - `/model/parse` Endpoint

## Overview

The Rasa API's `/model/parse` endpoint enables intent classification and entity extraction from text without considering conversation context. This endpoint is particularly useful for:

- Testing intent classification
- Verifying model accuracy
- Integration with systems that require only classification without maintaining conversation state

## API Specification

### Endpoint Details

- **URL**: `/model/parse`
- **Method**: POST
- **Content-Type**: application/json

### Request Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `text` | string | Yes | The text to be interpreted by the NLU model |

### Request Example

**cURL**

```bash
curl --location 'http://localhost:5005/model/parse' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Hello, how are you?"
}'
```

### Response Example
```json
{
    "text": "Hello, how are you?",
    "intent": {
        "name": "greeting",
        "confidence": 0.99
    },
    "entities": [],
    "text_tokens": [
        [
            0,
            5
        ],
        [
            7,
            10
        ],
        [
            11,
            14
        ]
    ],
    "intent_ranking": [
        {
            "name": "greeting",
            "confidence": 0.99
        },
        {
            "name": "goodbye",
            "confidence": 0.01
        }
    ],
    "response_selector": {
        "all_retrieval_intents": [],
        "default": {
            "response": {
                "responses": null,
                "confidence": 0.0,
                "intent_response_key": null,
                "utter_action": "utter_None"
            },
            "ranking": []
        }
    }
}
```

### Response Structure
| Field | Type | Description |
|-------|------|-------------|
| `text` | string | The original text sent for analysis |
| `intent` | object | The primary identified intent, containing `name` and `confidence` |
| `entities` | array | List of entities extracted from the text |
| `text_tokens` | array | Tokens identified in the text with their positions |
| `intent_ranking` | array | Ranking of all intents with their respective scores |
| `response_selector` | object | Information about response selection for retrieval intents |

## Difference Between `/model/parse` and Other Conversational Endpoints

The `/model/parse` endpoint does **not** maintain conversation state and doesn't consider previous messages. It is used exclusively for:

- Classifying user intent in a single message
- Extracting entities from an isolated message
- Evaluating the model's effectiveness in recognizing specific patterns

## Best Practices

- Use this endpoint only for isolated classification, not for maintaining conversations
- For model accuracy testing, compare results with expected ground truth
- Monitor confidence scores to identify cases of low certainty
- Consider a minimum confidence threshold for accepting classification (typically above 0.6)
- Use this endpoint for batch testing of your NLU model with a test dataset

## Additional Resources

- [Complete Rasa API Documentation](https://rasa.com/docs/reference/api/)
- [Rasa NLU Guide](https://rasa.com/docs/rasa/nlu/about/)
- [Rasa API](https://rasa.com/docs/reference/api/pro/http-api/)
- [Training Data Format](https://rasa.com/docs/rasa/nlu-training-data/)