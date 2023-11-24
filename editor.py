
class TextEditor:
    def __init__(self, directory='content'):
        self.directory = directory

    def get_text_files(self):
        """Retorna uma lista de arquivos .txt na pasta content, ordenados numericamente."""
        from pathlib import Path
        
        # Acessa o diretório e lista todos os arquivos .txt
        path = Path(self.directory)
        text_files = sorted(path.glob('*.txt'), key=lambda x: int(x.stem.replace('chapter', '')))
        return text_files

    def concatenate_texts(self):
        text_files = self.get_text_files()
        combined_text = ''
        
        for text_file in text_files:
            # Tente abrir com a codificação padrão UTF-8 primeiro
            try:
                with open(text_file, 'r', encoding='utf-8') as file:
                    combined_text += file.read() + '\n'
            except UnicodeDecodeError:
                # Se falhar, tente outras codificações comuns
                encodings = ['iso-8859-1', 'windows-1252', 'utf-16']
                for encoding in encodings:
                    try:
                        with open(text_file, 'r', encoding=encoding) as file:
                            combined_text += file.read() + '\n'
                        break  # Se sucesso, saia do loop de codificações
                    except UnicodeDecodeError:
                        continue  # Se falhar, tente a próxima codificação
                else:
                    # Se todas as codificações falharem, levante uma exceção
                    raise UnicodeDecodeError(f"Cannot decode file {text_file} with any of the tried encodings.")
        
        return combined_text


    def save_to_ebook(self, combined_text):
        """Salva o texto concatenado em um arquivo chamado 'ebook.txt'."""
        ebook_path = self.directory + '/ebook.txt'
        
        with open(ebook_path, 'w', encoding='utf-8') as file:
            file.write(combined_text)
            
if __name__ == "__main__":
    editor = TextEditor()
    combined_text = editor.concatenate_texts()
    editor.save_to_ebook(combined_text)