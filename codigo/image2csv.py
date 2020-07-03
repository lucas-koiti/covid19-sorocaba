"""
    Criação da planilha apenas com algumas imagens, pois a prefeitura mudou de padrao para divulgação 3 vezes.
    Alguns erros de identificação pelo pytesseract corrigidos manualmente. 
"""
import os
import csv
import pytesseract
from PIL import Image


# configuracao para o tesseract identificar numeros
custom_config = r'--oem 3 --psm 8 outputbase digits'

# linhas da planilha
csvrows = []

# percorre cada imagem da pasta /dados/imagens/tipo2
for entry in os.scandir(r'../dados/imagens/tipo2'):
    if(entry.path.endswith(".jpg") and entry.is_file()):

        image = Image.open(entry.path)

        # isola um retangulo
        top = 450
        bottom = 502

        # isola o quadro casos confirmados
        left = 155
        right = 310
        confirmados = image.crop((left,top,right,bottom))
        conf = (pytesseract.image_to_string(confirmados, lang='por', config=custom_config))
        # isola o quadro obitos 900
        left = 350
        right = 470
        obitos = image.crop((left,top,right,bottom))
        obt = (pytesseract.image_to_string(obitos, lang='por', config=custom_config))
        # isola o quadro internados
        left = 530
        right = 645
        internados = image.crop((left,top,right,bottom))
        inter = (pytesseract.image_to_string(internados, lang='por', config=custom_config))
        # isola o quadro recuperados
        left = 715
        right = 885
        recuperados = image.crop((left,top,right,bottom))
        rec = (pytesseract.image_to_string(recuperados, lang='por', config=custom_config))
        
        dia = int(entry.path[-7:-4])
        row = [dia, conf, obt, inter, 0, rec]

        csvrows.append(row.copy())

# ordena a lista de linhas pela data, pois o os.scandir itera de forma arbitraria
csvrows.sort(key=lambda x: x[0])
csvrows.insert(0, ['Dia', 'Confirmados', 'Obitos', 'Recuperacao', 'Recuperados'])

# cria a planilha na pasta dados/planilha_csv
with open('../dados/planilha_csv/dados.csv', 'w', newline='') as planilha:
    wr = csv.writer(planilha, quoting = csv.QUOTE_ALL)
    for row in csvrows:
        wr.writerow(row)