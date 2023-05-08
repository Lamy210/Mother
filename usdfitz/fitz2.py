import PyPDF2

# 入力ファイルを開く
with open('./rsy2023sem1_GP21A122-5.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # 出力ファイルを開く
    with open('output.pdf', 'w') as out_file:
        writer = PyPDF2.PdfWriter()
        # 指定されたページの一部を切り抜く
        page = reader.pages[0]
        page.cropbox.upperRight = (page.cropbox.upperRight[750])
        page.cropbox.lowerLeft = (page.cropbox.getLowerLeft, 600)
        writer.addpage(page)
        writer.write(out_file)
