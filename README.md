
# Gerador de eBook

## Descrição

O **Gerador de eBook** é um projeto que automatiza a criação de eBooks a partir de capítulos em texto. Ele utiliza diversos scripts em Python para compilar, editar e formatar o conteúdo, resultando em um eBook final em PDF.

## Instalação

Para instalar e executar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/gerador-ebook.git
    cd gerador-ebook
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Uso

Para gerar seu eBook, siga os passos abaixo:

1. Certifique-se de que todos os capítulos estejam no diretório correto (`content`).
2. Execute o script principal para compilar o eBook:
    ```bash
    python app.py
    ```
3. O eBook gerado será salvo como `ebook.pdf` no diretório raiz do projeto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests. Para contribuir:

1. Faça um fork do projeto
2. Crie uma nova branch com sua feature:
    ```bash
    git checkout -b minha-feature
    ```
3. Commit suas mudanças:
    ```bash
    git commit -m 'Adiciona minha feature'
    ```
4. Envie para a branch original:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
