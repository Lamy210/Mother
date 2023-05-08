import PyPDF2
import chardet

# PDFファイルを開く
#pdf_file = open('./rsy2023sem1_GP21A122-5.pdf', 'rb')
with open('./rsy2023sem1_GP21A122-5.pdf', 'rb') as pdf_file:

    # PDFファイルを読み込む
    pdf_reader =PyPDF2.PdfReader(pdf_file)

    # 1ページ目のテキストを抽出する
    page = pdf_reader.pages[0]
    text = page.extract_text()

    # テキストの文字コードを検出する
    encoding = chardet.detect(text.encode())['encoding']

    # PDFファイルを閉じる
    pdf_file.close()

# 文字コードを表示する
print(encoding)
