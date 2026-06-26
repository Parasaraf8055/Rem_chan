class MoodManager:

    def __init__(self):

        self.mood = "happy"

    def set_mood(
        self,
        mood
    ):

        self.mood = mood

    def get_mood(self):

        return self.mood