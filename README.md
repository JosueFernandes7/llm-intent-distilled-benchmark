https://rasa.com/docs/reference/api/pro/http-api/#tag/Model/operation/predictModelAction`

## Utilizando a model/parse que é uma rota do rasa para que se use somente a classificação, sem interação de contexto do chatbot, ou seja utilizada somente para averiguar a classificação
Requisição


1. 
    cURL
    ```bash
    curl --location 'http://localhost:5005/model/parse' \
    --header 'Content-Type: application/json' \
    --data '{
        "text": "Olá, tudo bem?"
    }'

    ```

2. Http
    POST http://localhost:5005/model/parse
    Body
    ```python
    {
        "text": "Olá, tudo bem?"
    }
    ```

Resposta
```javascript
{
    "text": "Olá, tudo bem?",
    "intent": {
        "name": "saudacao",
        "confidence": 1.0
    },
    "entities": [],
    "text_tokens": [
        [
            0,
            3
        ],
        [
            5,
            9
        ],
        [
            10,
            13
        ]
    ],
    "intent_ranking": [
        {
            "name": "saudacao",
            "confidence": 1.0
        },
        {
            "name": "falar_com_atendente_humano",
            "confidence": 8.816684604617819e-10
        },
        {
            "name": "solicitar_informacoes_produto",
            "confidence": 7.778560018323333e-10
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
