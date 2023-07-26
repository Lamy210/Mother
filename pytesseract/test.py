import pytesseract
from PIL import Image
image = Image.open('sample.png')

# 画像からテキストを抽出（日本語と英語）
text = pytesseract.image_to_string(image, lang='jpn+eng')
print(text)