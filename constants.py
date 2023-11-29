# constants.py

OPENAI_KEY = ''
CHARACTER = 'Agora você é um escritor/redator de ebooks com temas interessantes, uma linguagem moderna e comercial.'

DESCRIPTION = 'Agora você é um escritor/redator de ebooks com temas interessantes, uma linguagem moderna e comercial.'

# List of questions and possible options
QUESTIONS = {
    "ebook_category": {
        "question": "Categoria do seu ebook:",
        "options": [
            "Receitas e gastronomia",
            "Tecnologia",
            "Autoajuda",
            "Marketing Digital e Negócios",
            "Viagem e turismo",
            "Livros infantil"
        ]
    },
    "ebook_title": {"question": "Título do e-book:"},
    "ebook_theme": {"question": "Tema do e-book:"},
    "image_style": {
        "question": "Estilo da imagem:",
        "options": [
            "Banco de imagens",
            "Ilustrações",
            "Foto realista de studio",
            "Estilo anime",
            "Ilustração infantil"
        ]
    },
    "page_count": {"question": "Quantidade de páginas:"},
    "language_style": {
        "question": "Estilo da linguagem:",
        "options": [
            "Jovem",
            "Técnica",
            "Profissional",
            "Clássica"
        ]
    },
    "author_name": {"question": "Nome do autor:"}
}


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Caminho para a pasta com as fontes Alegreya Sans
FONTS_PATH = 'fontes/'

# Registrar as variações da fonte Alegreya Sans no ReportLab
def register_fonts():
    pdfmetrics.registerFont(TTFont('AlegreyaSans-Regular', FONTS_PATH + 'AlegreyaSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-Italic', FONTS_PATH + 'AlegreyaSans-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-Bold', FONTS_PATH + 'AlegreyaSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-BoldItalic', FONTS_PATH + 'AlegreyaSans-BoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-Black', FONTS_PATH + 'AlegreyaSans-Black.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-BlackItalic', FONTS_PATH + 'AlegreyaSans-BlackItalic.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-ExtraBold', FONTS_PATH + 'AlegreyaSans-ExtraBold.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-ExtraBoldItalic', FONTS_PATH + 'AlegreyaSans-ExtraBoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-Light', FONTS_PATH + 'AlegreyaSans-Light.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-LightItalic', FONTS_PATH + 'AlegreyaSans-LightItalic.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-Medium', FONTS_PATH + 'AlegreyaSans-Medium.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-MediumItalic', FONTS_PATH + 'AlegreyaSans-MediumItalic.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-Thin', FONTS_PATH + 'AlegreyaSans-Thin.ttf'))
    pdfmetrics.registerFont(TTFont('AlegreyaSans-ThinItalic', FONTS_PATH + 'AlegreyaSans-ThinItalic.ttf'))

# Chamada a função para registrar as fontes
register_fonts()
