import PyPDF2

# PDFファイルを開く
pdf_file = open('./sample.pdf', 'rb')

# PDFリーダーオブジェクトを作成
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# ページオブジェクトを取得
page = pdf_reader.getPage(0)

# ページのテキストを取得
text = page.extractText()

# 検索する文字列を指定
search_string = "example"

# 検索する文字列の座標を取得
x0, y0, x1, y1 = None, None, None, None
for word in text.split():
    if search_string in word:
        x0, y0, x1, y1 = page.getCharBoundingBox(word)
        break

# 座標を表示
print(f"x0={x0}, y0={y0}, x1={x1}, y1={y1}")

# ファイルを閉じる
pdf_file.close()
