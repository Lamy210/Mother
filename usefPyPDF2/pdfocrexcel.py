from flask import Flask, render_template
import pytesseract
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # PDFファイルをOCRで処理して、テキストを抽出する
    text = pytesseract.image_to_string('./book1.pdf', lang='jpn')


    # テキストデータを整形して、必要な情報を抽出する
    lines = text.split('\n')
    target_data = []
    for line in lines:
        if '対象の情報' in line:
            target_data.append(line)
            break
    for line in lines:
        if '価格' in line:
            target_data.append(line)
            break

    # Excelファイルを読み込んで、必要な情報を抽出する
    df = pd.read_excel('./Book1.xlsx')
    relevant_data = df.loc[df['商品名'] == '対象の商品名']
    relevant_price = relevant_data['価格'].values[0]

    # OCRで抽出した情報とExcelから抽出した情報を照合し、必要なデータを取得する
    target_price = None
    for data in target_data:
        if '¥' in data:
            target_price = int(data.split('¥')[1].replace(',', ''))
            break

    if target_price and relevant_price and target_price == relevant_price:
        result = '一致しています'
    else:
        result = '一致していません'

    # 結果をウェブサイトに出力する
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
