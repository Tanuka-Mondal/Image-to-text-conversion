import pytesseract as pt
import os
from PIL import Image

pt.pt.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def convert():
    img = Image.open('img.jpg')
    text = pt.image_to_string(img)
    print(text)

convert()    
