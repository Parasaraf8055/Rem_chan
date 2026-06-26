import json
import os


class ConversationManager:

    def __init__(self):

        self.file_path = (
            "data/conversation_history.json"
        )

        self.load()

    def load(self):

        if not os.path.exists(
            self.file_path
        ):

            self.history = []

            self.save()

        else:

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.history = json.load(
                    file
                )

    def save(self):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.history,
                file,
                indent=4
            )

    def add_message(
        self,
        role,
        message
    ):

        self.history.append(
            {
                "role": role,
                "message": message
            }
        )

        self.history = (
            self.history[-5:]
        )

        self.save()

    def get_context(self):

        context = ""

        for item in self.history:

            context += (
                f"{item['role']}: "
                f"{item['message']}\n"
            )

        return context