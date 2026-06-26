import json
import os


class MemoryManager:

    def __init__(self):

        self.memory_file = (
            "data/memories.json"
        )

        self.load_memory()

    def load_memory(self):

        if not os.path.exists(
            self.memory_file
        ):

            self.memory = {}

            self.save_memory()

        else:

            with open(
                self.memory_file,
                "r"
            ) as file:

                self.memory = json.load(
                    file
                )

    def save_memory(self):

        with open(
            self.memory_file,
            "w"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )

    def remember(
        self,
        key,
        value
    ):

        self.memory[key] = value

        self.save_memory()

    def recall(
        self,
        key
    ):

        return self.memory.get(
            key,
            None
        )