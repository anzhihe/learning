import pytesseract
from PIL import Image
  
# 打开图片
image = Image.open('example.png')

# OCR识别：lang指定中文,--psm 6 表示按行识别，有助于提升识别准确率
text = pytesseract.image_to_string(image, lang="chi_sim+eng", config='--psm 6')

# 打印识别后的文本
print(text)