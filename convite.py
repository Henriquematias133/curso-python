from PIL import Image, ImageDraw, ImageFont
from IPython.display import Image as imgx

nomes = ['Henrique', 'Jeferson', 'Vitor']
Evento ='Formatura do Python'
Data = '27 de Fevereiro de 2025'
Local = ' Av Paulista, na Clarify'

for nome in nomes:
    # criando uma imagem em rgb com fundo branco (600 por 400px)
    img = Image.new("RGB",(600,400),(255,255,255))
    draw = ImageDraw.Draw(img) #preparando a ferramenta para desenhar a imagem

    # fonte que serã usadas no texto
    font_title=ImageFont.truetype("arial.ttf",36)
    # fonte do titulo e tamanho
    font_text=ImageFont.truetype("arial.ttf",24)
    #fonte para o texto do evento e tamanho
    #adicionando o texto principal na imagem(titulo do convite com nome)

    draw.text((50,50), f'Convite de Formatura para {nome}',(0,0,0), fonte=font_title)

    draw.text((50,100), Evento,(0,0,0), fonte=font_text)

    draw.text((50,150), Data,(0,0,0), fonte=font_text)

    draw.text((50,200), Local,(0,0,0), fonte=font_text)

    draw.rectangle([(45,45),(555,355)],outline=(0,0,0),width=5)

    img.save(f"{nome}.jpg")


