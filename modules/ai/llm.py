import google.generativeai as genai

from core.config_manager import load_settings

from core.memory_manager import (
    MemoryManager
)

from core.memory_extractor import (
    MemoryExtractor
)

from core.profile_manager import (
    ProfileManager
)

from core.conversation_manager import (
    ConversationManager
)

from core.prompt_builder import (
    PromptBuilder
)


class RemBrain:

    def __init__(self):

        settings = load_settings()
        genai.configure(
            api_key=settings["gemini_api_key"]
        )

        self.memory = (
            MemoryManager()
        )

        self.prompt_builder = (
            PromptBuilder()
        )

        self.conversation = (
            ConversationManager()
        )

        self.extractor = (
            MemoryExtractor()
        )

        self.profile = (
            ProfileManager()
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )



    def ask(self, user_message):

        msg = user_message.lower()

        if (
            "what is my name" in msg
            or "who am i" in msg
        ):

            name = (
                self.profile.get_name()
            )
            print(
            "LOCAL MEMORY ANSWER"
        )
            if name:

                return (
                    f"Your name is "
                    f"{name}, Master. 💙"
                )

            return (
                "I do not know your name yet, Master."
            )
        
        if (
            "what are my interests" in msg
            or "what do i like" in msg
        ):
            print(
                "LOCAL MEMORY ANSWER"
            )
            interests = (
                self.profile.get_interests()
            )

            if interests:

                return (
                    "You are interested in: "
                    + ", ".join(interests)
                    + " 💙"
                )

            return (
                "You haven't shared your interests yet, Master."
            )
        
        if (
            "what project am i building" in msg
            or "what are my projects" in msg
        ):
            print(
                "LOCAL MEMORY ANSWER"
            )
            projects = (
                self.profile.get_projects()
            )

            if projects:

                return (
                    "You are working on: "
                    + ", ".join(projects)
                )

            return (
                "I don't know any projects yet, Master."
            )
        
        if (
            "what are my goals" in msg
        ):
            print(
                "LOCAL MEMORY ANSWER"
            )
    
            goals = (
                self.profile.get_goals()
            )

            if goals:

                return (
                    "Your goals are: "
                    + ", ".join(goals)
                )

            return (
                "You haven't told me your goals yet, Master."
            )
        
        if (
            "what is my startup" in msg
        ):
            print(
                "LOCAL MEMORY ANSWER"
            )

            startup = (
                self.profile.get_startup()
            )

            if startup:

                return (
                    f"Your startup is "
                    f"{startup}, Master."
                )

            return (
                "I don't know your startup yet."
            )
        memories = (
            self.extractor.extract(
                user_message
            )
        )

        if "name" in memories:

            self.profile.set_name(
                memories["name"]
            )

        if "interest" in memories:

            self.profile.add_interest(
                memories["interest"]
            )

        if "project" in memories:
            self.profile.add_project(
                memories["project"]
            )

        if "startup" in memories:
            self.profile.set_startup(
                memories["startup"]
            )

        if "goal" in memories:
            self.profile.add_goal(
                memories["goal"]
            )

        print("USER MESSAGE:", user_message)


        stored_name = (
            self.profile.get_name()
        )

        stored_interest = (
            self.profile.get_interests()
        )

        conversation_context = (
            self.conversation.get_context()
        )

        
        system_prompt = (
            self.prompt_builder.build(
                user_message,
                self.profile,
                conversation_context
            )
        )

        self.conversation.add_message(
            "User",
            user_message
        )

        
        
        try:


            response = self.model.generate_content(
                system_prompt,
                generation_config={
                    "temperature": 0.7
                   
                }
            )

            self.conversation.add_message(
                "Assistant",
                response.text
            )

            return response.text


        except Exception as e:


            print(e)

            return (
                "Master, my connection to the AI "
                "brain is temporarily exhausted. "
                "Please wait a little while and "
                "try again. 💙"
            )



       

        