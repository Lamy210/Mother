import PyPDF2
import chardet

# PDFファイルを開く
pdf_file = open('./rsy2023sem1_GP21A122-5.pdf', 'rb')

# PdfFileReaderオブジェクトを作成する
pdf_reader = PyPDF2.PdfReader(pdf_file)

# ページ数を取得する
num_pages = len(pdf_reader.pages)

# 各ページのテキストを取得する
text = ''
for page_idx in range(num_pages):
    page = pdf_reader.pages[page_idx]
    text = page.extract_text()
    result= chardet.detect(text.encode())
    #decoded_text = text.decode(result['encoding'])


# 抽出したテキストを表示する
print(text)
#print(decoded_text)
