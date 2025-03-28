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
}
```


Pegar chave de api no mistral.ai

export MISTRAL_KEY="SUA-CHAVE"