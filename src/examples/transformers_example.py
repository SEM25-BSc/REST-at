import os
from dotenv import load_dotenv
from ..util import model as ml


def main() -> None:
    load_dotenv()

    # Model data
    model_id: str = os.getenv("MODEL_PATH")
    max_new_tokens: int = 4096

    # Load model
    model : ml.Model = ml.Model.load(model_id, max_new_tokens)

    # Create an empty message history
    messages: list[dict[str, str]] = []

    # Chat loop
    user_prompt: str = ""
    while user_prompt.lower() != "bye":
        user_prompt = input("> ")
        res = model.prompt(messages, user_prompt)
        print(f"\nLLM> {res}\n")


if __name__ == "__main__":
    main()
