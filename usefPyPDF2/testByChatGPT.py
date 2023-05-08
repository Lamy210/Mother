import PyPDF2

# PDFファイルを開く
with open('./rsy2023sem1_GP21A122-5.pdf', 'rb') as pdf_file:

    # PDFリーダーオブジェクトを作成
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # ページオブジェクトを取得
    page = pdf_reader.pages[0]

    # 座標を指定してページを切り抜く
    left_x = 100
    bottom_y = 100
    right_x = 400
    top_y = 400
    page.cropbox.lower_Left = (left_x, bottom_y)
    page.cropbox.upper_right = (right_x, top_y)

    # 切り抜いたページを新しいPDFファイルに保存
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page)
    with open('output.pdf', 'wb') as new_pdf_file:
        pdf_writer.write(new_pdf_file)