import pytesseract
from PIL import Image


i='WEB.png'
im=Image.open(f'C:\\Users\\ECI170\\Desktop\\{i}')
#print(pytesseract.image_to_string(im))
#指定图像中的语言-中文
print(pytesseract.image_to_string(im))

#txt=open(f'C:\\Users\\ECI170\\Desktop\\ocr.txt',mode='w+')
#txt.write(pytesseract.image_to_string(im))
#txt.close()
