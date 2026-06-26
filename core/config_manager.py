import os
import json

from dotenv import load_dotenv

load_dotenv()


def load_settings():

    with open(
        "config/settings.json",
        "r"
    ) as file:

        settings = json.load(file)

    settings["gemini_api_key"] = os.getenv(
        "GEMINI_API_KEY"
    )

    return settings