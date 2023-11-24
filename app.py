import json
from constants import QUESTIONS, OPENAI_KEY
from interaction import UserInteraction
from prompt import PromptManager
from script import EbookChapterGenerator
from extract import ContentExtractor
from generator import EbookContentGenerator  # Importação adicionada

def save_responses_to_json(responses, filename='data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(responses, f, ensure_ascii=False, indent=4)

def main():
    # Coleta as respostas do usuário
    user_interaction = UserInteraction(QUESTIONS)
    user_responses = user_interaction.get_user_responses()
    
    # Salva as respostas no arquivo JSON
    save_responses_to_json(user_responses)
    
    # Cria uma instância da classe PromptManager
    prompt_manager = PromptManager('data.json')
    
    # Obtém os detalhes necessários para gerar o prompt
    ebook_title, ebook_theme, page_count = prompt_manager.get_ebook_details()
    
    # Gera o prompt com os detalhes coletados
    prompt = prompt_manager.generate_prompt(ebook_title, ebook_theme, page_count)
    
    # Salva o prompt gerado no arquivo JSON
    prompt_manager.save_prompt_to_data(prompt)
    
    # Cria uma instância da classe EbookChapterGenerator
    chapter_generator = EbookChapterGenerator('data.json')
    
    # Gera os capítulos usando a API da OpenAI
    api_response = chapter_generator.generate_chapters()
    
    # Salva a resposta da API no arquivo JSON, incluindo o conteúdo e o custo
    chapter_generator.save_api_response_to_file(api_response)

    # Cria uma instância da classe ContentExtractor
    content_extractor = ContentExtractor('data.json')
    
    # Extrai os capítulos da resposta da API
    chapters = content_extractor.extract_chapters()
    
    # Salva os capítulos extraídos no arquivo JSON
    content_extractor.save_chapters_to_data(chapters)

    # Cria uma instância da classe EbookContentGenerator e gera o conteúdo dos capítulos
    ebook_content_generator = EbookContentGenerator(language_style='Jovem')
    chapters = ebook_content_generator.load_chapters('data.json')
    ebook_content_generator.generate_prompts(chapters)
    ebook_content_generator.create_chapter_contents(ebook_content_generator.prompt_content)

    # Informa ao usuário que o processo de geração do e-book está completo
    print("Aguarde, vamos gerar o seu e-book...")

if __name__ == "__main__":
    main()
