import pandas as pd
from reportlab.lib.pagesizes import A3  # A3用紙サイズをインポート
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# CSVファイルを読み込む
data = pd.read_csv('textbook_GP18A000_list.csv', encoding='utf-8')

# 日本語フォントを登録する
font_path = 'C:\\Windows\\Fonts\\msgothic.ttc'
pdfmetrics.registerFont(TTFont('JapaneseFont', font_path))

# PDFを作成する
pdf = SimpleDocTemplate('textbook_GP18A000_list.pdf', pagesize=A3, topMargin=50, bottomMargin=50)

# テーブルのデータを準備する
table_data = [data.columns.tolist()]  # ヘッダーを追加

for _, row in data.iterrows():
    table_data.append(row.tolist())

# テーブルスタイルを設定する
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # ヘッダーの背景色
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # ヘッダーテキストの色
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # テキストの配置
    ('FONTNAME', (0, 0), (-1, 0), 'JapaneseFont'),  # ヘッダーフォント
    ('FONTSIZE', (0, 0), (-1, 0), 11),  # ヘッダーフォントサイズを11に変更
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # ヘッダーの下側パディング
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # テーブルの背景色
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # グリッド線の設定
])

# テーブルを作成し、スタイルを適用する
table = Table(table_data)
table.setStyle(table_style)

# テーブル内の文字のスタイルを設定する
styles = getSampleStyleSheet()
cell_style = styles['BodyText']
cell_style.fontName = 'JapaneseFont'
cell_style.fontSize = 9  # フォントサイズを9に変更

for i in range(1, len(table_data)):
    for j in range(len(table_data[i])):
        table.setStyle([('FONTNAME', (j, i), (j, i), 'JapaneseFont')])

# ページごとにテーブルを分割して表示する
pdf_content = []
row_index = 0
rows_per_page = 45  # 1ページあたりの行数

while row_index < len(table_data):
    current_page_rows = table_data[row_index:row_index + rows_per_page]
    if row_index > 0:
        pdf_content.append(PageBreak())  # ページ区切り

    table = Table(current_page_rows)
    table.setStyle(table_style)
    table.setStyle([('FONTNAME', (0, 0), (-1, 0), 'JapaneseFont')])  # ヘッダーフォント
    table.setStyle([('FONTSIZE', (0, 0), (-1, 0), 11)])  # ヘッダーフォントサイズを11に変更
    table.setStyle([('BOTTOMPADDING', (0, 0), (-1, 0), 12)])  # ヘッダーの下側パディング

    for i in range(1, len(current_page_rows)):
        for j in range(len(current_page_rows[i])):
            table.setStyle([('FONTNAME', (j, i), (j, i), 'JapaneseFont')])

    pdf_content.append(table)
    row_index += rows_per_page

# PDFを保存する
pdf.build(pdf_content)

#PDFの変換