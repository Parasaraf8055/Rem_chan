import os

class AnimationManager:

    def __init__(self):

        self.animations = {
            "idle": self.load_frames(
                "assets/images/rem_idle"
            ),
            "walk": self.load_frames(
                "assets/images/rem_walk"
            )
        }

    def load_frames(self, folder):

        frames = []

        if not os.path.exists(folder):
            return frames

        files = sorted(
            os.listdir(folder),
            key=lambda x: x.lower()
        )

        for file in files:

            if file.endswith(".png"):

                frames.append(
                    os.path.join(folder, file)
                )

        return frames

    def get_animation(self, state):

        return self.animations.get(state, [])