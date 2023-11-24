# prompt.py

import json

class PromptManager:
    def __init__(self, data_filename='data.json'):
        self.data_filename = data_filename

    def get_ebook_details(self):
        with open(self.data_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['ebook_title'], data['ebook_theme'], data['page_count']

    def generate_prompt(self, ebook_title, ebook_theme, page_count):
        prompt = (
            f"Estou planejando criar um e-book com o título '{ebook_title}' sobre '{ebook_theme}', "
            f"com um total de {page_count} páginas. Por favor, crie uma estrutura detalhada para este e-book, "
            "incluindo títulos de capítulos e uma breve descrição para cada um, "
            "seguindo um formato onde cada capítulo e sua descrição estejam entre chaves {}, "
            "e a descrição entre colchetes []. "
            "Por exemplo: {Capítulo 1:} [Descrição do capítulo]."
        )
        return prompt

    def save_prompt_to_data(self, prompt):
        with open(self.data_filename, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data['prompt'] = prompt
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()  
            