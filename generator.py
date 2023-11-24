import json
import openai
from constants import OPENAI_KEY

class EbookContentGenerator:
    def __init__(self, language_style):
        self.language_style = language_style
        self.prompt_content = {}
        openai.api_key = OPENAI_KEY

    def load_chapters(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:  # Adicione 'encoding='utf-8''
            data = json.load(file)
        return data.get("chapters", {})


    def generate_prompts(self, chapters):
        for chapter_title, chapter_content in chapters.items():
            prompt = (
                f"Agora, crie o conteúdo com o seguinte tema: '{chapter_content}'.\n"
                f"O conteúdo precisa ter o tom '{self.language_style}'.\n\n"
                "Sua resposta deve seguir essa estrutura:\n\n"
                "* Título entre chaves.\n"
                "* Notas ou dicas entre asteriscos.\n"
                "* Itens de destaque em negrito."
            )
            self.prompt_content[chapter_title] = prompt

    def create_chapter_contents(self, prompts):
        chapter_number = 0
        for chapter_title, prompt in prompts.items():
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {
                        "role": "system",
                        "content": "DESCRIPTION"
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=1,
                max_tokens=9024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            chapter_number += 1
            filename = f"chapter{str(chapter_number).zfill(2)}.txt"
            with open(filename, 'w') as file:
                file.write(response['choices'][0]['message']['content'])

        print("Seu ebook foi gerado com sucesso.")

# Usage
if __name__ == "__main__":
    generator = EbookContentGenerator(language_style='Jovem')
    chapters = generator.load_chapters('data.json')
    generator.generate_prompts(chapters)
    generator.create_chapter_contents(generator.prompt_content)
