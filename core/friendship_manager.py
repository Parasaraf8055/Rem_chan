class FriendshipManager:

    def __init__(self):

        self.friendship = 0

    def increase(self, amount=1):

        self.friendship += amount

        
        print(
            f"💙 Friendship Level: {self.friendship}"
    )
        