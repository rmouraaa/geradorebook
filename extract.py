# extract.py

import json
import re

class ContentExtractor:
    def __init__(self, data_filename='data.json'):
        self.data_filename = data_filename

    def get_api_content(self):
        with open(self.data_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('api_content', '')

    def extract_chapters(self):
        content = self.get_api_content()
        # This regex looks for content between {Chapter X:} [Description]
        chapters = re.findall(r'\{(.*?)\}\s*\[(.*?)\]', content)
        return {f'Chapter {i+1}': description for i, (_, description) in enumerate(chapters)}

    def save_chapters_to_data(self, chapters):
        with open(self.data_filename, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data['chapters'] = chapters
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()  # Remove remaining part of old data if exists.
