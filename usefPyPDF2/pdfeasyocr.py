import io
import os
import tempfile
import easyocr
from pdf2image import convert_from_path

# PDFファイルのパス
pdf_path = './rsy2023sem1_GP21A122-5.pdf'

# PDFを画像に変換
with tempfile.TemporaryDirectory() as path:
    images = convert_from_path(pdf_path, output_folder=path)

    # 画像をEasyOCRで読み込む
    reader = easyocr.Reader(['ja'])
    texts = []
    for img in images:
        results = reader.readtext(np.array(img))
        for result in results:
            text = result[1]
            texts.append(text)

# テキストを出力
print('\n'.join(texts))
