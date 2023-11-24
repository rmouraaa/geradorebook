from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, BaseDocTemplate, PageTemplate, Frame, Image
from reportlab.platypus.flowables import Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from pathlib import Path
from constants import register_fonts  # Importando a função do módulo constants.py

# Registrar as fontes customizadas Alegreya Sans
register_fonts()

# Classe para criar um fundo de cor sólida em uma página
class Background(Flowable):
    def __init__(self, width, height, color):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, stroke=0, fill=1)

# Função para criar o PDF com margens personalizadas, estilos aprimorados e imagens
def create_pdf_with_styles_and_images(text_file_path, images_folder_path, output_filename, margin_points):
    # Configuração da página A4 com margens personalizadas
    page_width, page_height = A4
    doc = BaseDocTemplate(
        output_filename,
        pagesize=A4,
        leftMargin=margin_points,
        rightMargin=margin_points,
        topMargin=margin_points,
        bottomMargin=margin_points
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    background_color = colors.HexColor("#131313")
    enhanced_color = colors.HexColor("#EBAD48")
    # Atualize os estilos para usar as fontes Alegreya Sans
    topic_style = ParagraphStyle('TopicStyle', parent=styles['BodyText'], fontName='AlegreyaSans-Bold', textColor=enhanced_color)
    italic_style = ParagraphStyle('ItalicStyle', parent=styles['BodyText'], fontName='AlegreyaSans-Italic', textColor=enhanced_color)
    title_style = ParagraphStyle('TitleStyle', parent=styles['Title'], fontName='AlegreyaSans-Bold', fontSize=18,
                                 textColor=colors.HexColor('#BFA871'), spaceAfter=12, spaceBefore=6)
    highlight_style = ParagraphStyle('HighlightStyle', parent=styles['BodyText'], fontName='AlegreyaSans-Bold', textColor=colors.white)
    body_style = ParagraphStyle('BodyTextStyle', parent=styles['BodyText'], fontName='AlegreyaSans-Regular', textColor=colors.white)
    
    # Frame com margens personalizadas
    frame = Frame(margin_points, margin_points, page_width-2*margin_points, page_height-2*margin_points, id='normal')

    # Template com o fundo
    template = PageTemplate(id='test', frames=frame, onPage=lambda canvas, doc: Background(page_width, page_height, background_color).drawOn(canvas, 0, 0))
    doc.addPageTemplates([template])
    
    # Carregar o conteúdo do ebook do arquivo de texto
    with open(text_file_path, 'r', encoding='utf-8') as f:
        text_content = f.read()
    
    # Listar todas as imagens na pasta fornecida, assumindo que são do tipo JPG
    image_files = sorted(Path(images_folder_path).glob('*.jpg'))

    Story = []
    first_title = True  # Flag para evitar quebra de página antes do primeiro título
    image_counter = 0  # Contador para acompanhar qual imagem adicionar

    # Dividir o conteúdo em parágrafos e aplicar estilos
    paragraphs = text_content.split('\n')
    for para in paragraphs:
        if para.strip().startswith('{') and para.strip().endswith('}'):
            # Tratar como um título
            para_text = para.strip('{}')
            if not first_title:  # Se não for o primeiro título, adicionar quebra de página e imagem
                # Primeiro adicione uma quebra de página para a imagem
                Story.append(PageBreak())
                if image_counter < len(image_files):  # Se ainda houver imagens, adicionar uma nova
                    img_path = image_files[image_counter]
                    img = Image(str(img_path), width=297, height=520)  # Tamanho das imagens em pontos
                    img.hAlign = 'CENTER'
                    img.vAlign = 'MIDDLE'
                    Story.append(img)
                    image_counter += 1  # Incrementar o contador de imagens
                # Depois adicione outra quebra de página para o título
                Story.append(PageBreak())
            else:
                first_title = False
            Story.append(Paragraph(para_text, title_style))
        elif para.strip() == '':
            Story.append(Spacer(1, 12))
        else:
            if '**' in para:
                para_text = para.replace('**', '')
                Story.append(Paragraph(para_text, topic_style))
            elif '*' in para:
                para_text = para.replace('*', '')
                Story.append(Paragraph(para_text, highlight_style))
            elif '"' in para:
                para_text = para.replace('"', '')
                Story.append(Paragraph(para_text, italic_style))
            else:
                Story.append(Paragraph(para, body_style))
    
    # Construção do documento com os elementos
    doc.build(Story)

# Definição dos caminhos para o ebook e pasta de imagens
# Esses caminhos devem ser corrigidos para refletir a estrutura de diretórios do seu ambiente
ebook_text_path = 'ebook/ebook.txt'  # Caminho para o arquivo de texto do ebook
images_folder_path = 'images'  # Caminho para a pasta com imagens

# Definição do caminho para o arquivo de saída
output_pdf_path = 'ebook.pdf'

# Margens de 90 pontos
custom_margin_points = 90

# Criar o PDF com margens personalizadas, estilos aprimorados e imagens
create_pdf_with_styles_and_images(ebook_text_path, images_folder_path, output_pdf_path, custom_margin_points)
