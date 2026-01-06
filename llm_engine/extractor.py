import json
from jsonschema import validate, ValidationError
from llm_engine.prompt import SYSTEM_PROMPT, build_user_prompt
from validation.schema import MCQ_SCHEMA

def extract_mcqs(llm_client, text: str, max_retries: int = 2):
    user_prompt = build_user_prompt(text)

    for attempt in range(max_retries + 1):
        response = llm_client.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt
        )

        try:
            parsed_output = json.loads(response)
            validate(instance=parsed_output, schema=MCQ_SCHEMA)
            return parsed_output

        except (json.JSONDecodeError, ValidationError):
            if attempt == max_retries:
                raise ValueError(
                    "LLM output failed schema validation after retries"
                )
