#coding:utf-8
import os
import pyocr
from PIL import Image
from pytesseract import pytesseract
image = Image.open('code.png')
pytesseract.tesseract_cmd = 'c:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
code = pytesseract.image_to_string(image)
print code
