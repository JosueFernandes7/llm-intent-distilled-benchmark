FEW_SHOT_PROMPT = """
You are an intent classifier.

Based on the examples below, classify the user input by choosing the most appropriate intent from the list of possible intents.

Available intents:
{intents}

Examples:
{examples}

User input: "{user_input}"

Respond ONLY with the name of the intent.
Do not explain your reasoning. Do not use any punctuation or extra text.
Just return the intent label, exactly as listed.
"""


ZERO_SHOT_PROMPT = """
You are an intent classifier.

Your task is to choose the most appropriate intent from the list below for the given user input.

Available intents:
{intents}

User input: "{user_input}"

Respond ONLY with the name of the intent.
Do not explain your choice, do not provide any extra text, and do not use quotes.
Just return the intent label, exactly as listed.
"""


SOFT_TARGET_PROMPT = """
You are an intent classification assistant.

Your task is to provide a probability distribution over the following possible intents for a given user input.

Return ONLY a valid JSON dictionary with intent-probability pairs, where values are between 0.0 and 1.0 and must sum to 1.0.

Available intents:
{intents}

User input: "{user_input}"

Respond only with a JSON object like:
{{"intent1": 0.35, "intent2": 0.25, "intent3": 0.40}}

Do not include any explanation, comments, or natural language.
"""

