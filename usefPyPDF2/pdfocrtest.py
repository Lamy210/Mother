import pytesseract
import pdf2image

# PDFファイルをイメージに変換する
def pdf_to_image(pdf_file):
    return pdf2image.convert_from_path(pdf_file)

# OCRを実行する
def ocr(image):
    return pytesseract.image_to_string(image)

# PDFをOCRしてテキストを抽出する
def pdf_ocr(pdf_file):
    images = pdf_to_image(pdf_file)
    text = ""
    for image in images:
        text += ocr(image)
    return text

# テスト
pdf_file = "./rsy2023sem1_GP21A122-5.pdf"
text = pdf_ocr(pdf_file)
print(text)
