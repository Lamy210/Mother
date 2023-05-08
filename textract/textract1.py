import textract

# PDFファイルからテキストを抽出
text = textract.process('./sample.pdf')

# 抽出したテキストを表示
print(text.decode('utf-8'))
