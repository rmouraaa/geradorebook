# content.py

import json
import time
import os
from constants import DESCRIPTION, OPENAI_KEY
import openai

class ContentGenerator:
    def __init__(self, data_filename='data.json'):
        self.data_filename = data_filename
        self.load_data()

    def load_data(self):
        # Import constants
        self.description = DESCRIPTION
        self.api_key = OPENAI_KEY
        # Load chapters and language style from data.json
        with open(self.data_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.chapters = data.get('chapters', {})
        self.language_style = data.get('language_style', 'neutral')

    def generate_prompt(self, chapter_title):
        prompt_content = f"""
        Agora, crie o conteúdo do capítulo '{chapter_title}'.
        O conteúdo precisa ter o tom '{self.language_style}'.

        Sua resposta deve seguir essa estrutura:

        * título do capítulo entre chaves.
        * Notas ou dicas entre asteriscos.
        * Itens de destaque em negrito.
        """
        return prompt_content.strip()

    def call_openai_api(self, prompt_content):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": self.description
                },
                {
                    "role": "user",
                    "content": prompt_content
                }
            ],
            temperature=1,
            max_tokens=9024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text.strip()

    def generate_and_save_content(self):
        # Ensure the 'content' directory exists
        if not os.path.exists('content'):
            os.makedirs('content')

        chapter_paths = {}
        for i, (chapter_title, _) in enumerate(self.chapters.items(), start=1):
            prompt_content = self.generate_prompt(chapter_title)
            chapter_content = self.call_openai_api(prompt_content)
            filename = f'content/capitulo{i:02d}.txt'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(chapter_content)
            chapter_paths[f'Chapter {i}'] = filename
            time.sleep(15)  # Pause for 15 seconds between API calls
        self.save_chapter_paths(chapter_paths)

    def save_chapter_paths(self, chapter_paths):
        with open(self.data_filename, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data['chapter_paths'] = chapter_paths
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
