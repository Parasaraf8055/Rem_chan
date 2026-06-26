import random


class MovementManager:

    def get_random_direction(self):

        return random.choice(
            [
                -1,
                1
            ]
        )