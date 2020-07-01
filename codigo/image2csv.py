#dependencies pillow e pytesseract

from PIL import Image
import pytesseract

image = Image.open("../dados/5_28.jpg")
left = 155
top = 450
right = 900
bottom = 502

image_1 = image.crop((left,top,right,bottom))


#image_1.show()

custom_config = r'--oem 3 --psm 13 outputbase digits'

output = (pytesseract.image_to_string(image_1, lang='por', config=custom_config))

print(output)