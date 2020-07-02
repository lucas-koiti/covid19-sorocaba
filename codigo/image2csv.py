import os
import pytesseract

from PIL import Image

# configuracao para o tesseract identificar numeros
custom_config = r'--oem 3 --psm 8 outputbase digits'

# linhas da planilha
csvrow = [['Dia', 'Confirmados', 'Obitos', 'Recuperacao', 'Recuperados']]

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
        
        dia = entry.path[-6:-4]+'/'+entry.path[-7:-6]
        row = [dia, conf, obt, inter, 0, rec]

        csvrow.append(row.copy())

for i in csvrow:
    print(i)