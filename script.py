# script.py

import json
import openai
from constants import OPENAI_KEY, CHARACTER

class EbookChapterGenerator:
    def __init__(self, data_filename='data.json'):
        self.data_filename = data_filename

    def get_prompt(self):
        with open(self.data_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('prompt')

    def generate_chapters(self):
        prompt = self.get_prompt()
        openai.api_key = OPENAI_KEY

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": CHARACTER
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
        return response

    def save_api_response_to_file(self, api_response):
        content = api_response['choices'][0]['message']['content']  # Extrai o conteúdo da resposta
        usage = api_response['usage']  # Extrai as informações de uso

        with open(self.data_filename, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data['api_content'] = content  # Salva apenas o conteúdo
            data['api_usage'] = usage  # Salva as informações de uso
            f.seek(0)  # Reset file position to the beginning.
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()  # Remove remaining part of old data if exists.
