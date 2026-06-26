import json


class ProfileManager:

    def __init__(self):

        self.file = "data/memories.json"

        with open(
            self.file,
            "r"
        ) as f:

            self.profile = json.load(f)

    def save(self):

        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                self.profile,
                f,
                indent=4
            )

    def set_name(
        self,
        name
    ):

        self.profile["name"] = name

        self.save()

    def get_name(self):

        return self.profile["name"]

    def add_interest(
    self,
    interest_text
):

        interests = [
            x.strip()
            for x in interest_text.split(",")
        ]

        for interest in interests:

            if (
                interest
                and interest not in self.profile["interests"]
            ):

                self.profile["interests"].append(
                    interest
                )

        self.save()

    def get_interests(self):

        return self.profile["interests"]
    

    def add_projects(
    self,
    project_text
):

        projects = [
            x.strip()
            for x in project_text.split(",")
        ]

        for project in projects:

            if (
                project
                and project not in self.profile["projects"]
            ):

                self.profile["projects"].append(
                    project
                )

        self.save()
    
    def get_projects(self):

        return self.profile["projects"]
    
    def add_hobbies(
    self,
    hobby_text
):

        hobbies = [
            x.strip()
            for x in hobby_text.split(",")
        ]

        for hobby in hobbies:

            if (
                hobby
                and hobby not in self.profile["hobbies"]
            ):

                self.profile["hobbies"].append(
                    hobby
                )

        self.save()

    def get_hobbies(self):

        return self.profile["hobbies"]
    
    def add_goals(
    self,
    goal_text
):

        goals = [
            x.strip()
            for x in goal_text.split(",")
        ]

        for goal in goals:

            if (
                goal
                and goal not in self.profile["goals"]
            ):

                self.profile["goals"].append(
                    goal
                )

        self.save()
    
    def get_goals(self):

        return self.profile["goals"]
    

    def set_startups(
        self,
        startups
    ):

        self.profile["startups"] = startups

        self.save()

    def get_startups(self):

        return self.profile["startups"]