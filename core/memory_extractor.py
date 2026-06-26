import re

class MemoryExtractor:

    def extract(self, message):

        memories = {}

        msg = message.lower()

        # -------------------
        # Name Detection
        # -------------------

        name_patterns = [
            r"my name is (.+)",
            r"i am (.+)",
            r"i'm (.+)",
            r"call me (.+)",
            r"this is (.+)",
            r"i am your master (.+)"
        ]

        for pattern in name_patterns:

            match = re.search(
                pattern,
                msg
            )

            if match:

                memories["name"] = (
                    match.group(1)
                    .strip()
                    .title()
                )

                break

        # -------------------
        # Interest Detection
        # -------------------

        interest_patterns = [
            r"i like (.+)",
            r"i love (.+)",
            r"i am interested in (.+)",
            r"my interest is (.+)",
            r"my interests are (.+)",
            r"i enjoy (.+)",
            r"i am passionate about (.+)"
        ]

        for pattern in interest_patterns:

            match = re.search(
                pattern,
                msg
            )

            if match:

                memories["interest"] = (
                    match.group(1)
                    .strip()
                    .title()
                )

                break

        # -------------------
        # Project Detection
        # -------------------

        project_patterns = [
            r"i am building (.+)",
            r"my project is (.+)",
            r"i am working on (.+)",
            r"i have a project (.+)",
            r"my project is called (.+)",
            r"i am developing (.+)",
            r"i am creating (.+)",
            r"i am designing (.+)",
            r"creating a project (.+)"
        ]

        for pattern in project_patterns:

            match = re.search(
                pattern,
                msg
            )

            if match:

                memories["projects"] = (
                    match.group(1)
                    .strip()
                    .title()
                )

                break

        # -------------------
        # startu Detection
        # -------------------

        startup_patterns = [
            r"my startup is (.+)",
            r"i am starting (.+)",
            r"i am launching (.+)",
            r"i have a startup (.+)",
            r"my startup is called (.+)"
        ]

        for pattern in startup_patterns:

            match = re.search(
                pattern,
                msg
            )

            if match:

                memories["startup"] = (
                    match.group(1)
                    .strip()
                    .title()
                )

                break

        # -------------------
        # goals Detection
        # -------------------

        goal_patterns = [
            r"my goal is (.+)",
            r"i want to become (.+)",
            r"i want to build (.+)",
            r"my end goals are (.+)",
            r"my end goal is (.+)",
            r"i want to achieve (.+)",
            r"my dream is (.+)",
            r"my dreams are (.+)"
        ]    

        for pattern in goal_patterns:

            match = re.search(
                pattern,
                msg
            )

            if match:

                memories["goals"] = (
                    match.group(1)
                    .strip()
                    .title()
                )

                break

        return memories

