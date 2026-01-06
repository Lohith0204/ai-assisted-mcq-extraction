MCQ_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["question", "options", "correct_answer"],
        "properties": {
            "question": {
                "type": "string"
            },
            "options": {
                "type": "object",
                "required": ["a", "b", "c", "d"],
                "properties": {
                    "a": {"type": "string"},
                    "b": {"type": "string"},
                    "c": {"type": "string"},
                    "d": {"type": "string"}
                }
            },
            "correct_answer": {
                "type": ["string", "null"],
                "enum": ["a", "b", "c", "d", None]
            }
        }
    }
}
