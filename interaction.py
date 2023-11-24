# interaction.py

class UserInteraction:
    def __init__(self, questions):
        self.questions = questions

    def ask_question(self, question, options=None):
        print(question)
        if options:
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")
            answer = input("Escolha uma opção (número): ")
            try:
                # Ensure the user's choice is a valid option
                choice_idx = int(answer) - 1
                if 0 <= choice_idx < len(options):
                    return options[choice_idx]
                else:
                    print("Por favor, selecione um número válido.")
                    return self.ask_question(question, options)
            except ValueError:
                print("Por favor, insira um número.")
                return self.ask_question(question, options)
        else:
            return input()

    def get_user_responses(self):
        user_responses = {}
        for key, value in self.questions.items():
            options = value.get("options")
            user_responses[key] = self.ask_question(value["question"], options)
        return user_responses
