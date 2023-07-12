from flask import Flask, render_template,request, jsonify,session
from werkzeug.utils import secure_filename
from pathlib import Path
from flask_cors import CORS
import secrets
import json
import base64
import PyPDF2
from pdf2image import convert_from_path
import os


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # 16バイトのランダムな値を生成
def allowed_file(filename):
    # 受け入れる拡張子のリスト
    allowed_extensions = ['jpeg', 'pdf', 'jpg', 'png']
    # ファイルの拡張子を取得
    extension = filename.rsplit('.', 1)[1].lower()
    # 拡張子が許可されたリストに含まれているかチェック
    return '.' in filename and extension in allowed_extensions
def file_extension(file_name):
    exten = file_name.split(".")[-1]
    return exten


def upload_file():
    # リクエストからファイルを取得
    file = request.files['file']
    if file and allowed_file(file.filename):
        # ファイルを保存する場所を指定
        file.save('./test/' + secure_filename(file.filename))





    ##########################################
    #セッションの処理を追加する




    ###########################################



        # レスポンスを返す
        return jsonify({'Message': 'ファイルがアップロードされました: [' + file + ']'})
    else:
        return jsonify({'Error': '対象外のファイル形式かもしれえんから確認してほしい'})
def K_PDF(file_name,output_name):    
    '''
    with open(file_name, 'rb') as pdf_file:
    # PDFリーダーオブジェクトを作成
        pdf_reader = PyPDF2.PdfReader(pdf_file)
    # ページオブジェクトを取得
    page = pdf_reader.pages[0]
    # 座標を指定してページを切り抜く     

    #ここの設定まだです。申し訳ないです。


    left_x = 0#??/
    bottom_y = 100
    right_x =0
    top_y = 300








    page.cropbox.lower_Left = (left_x, bottom_y)
    page.cropbox.upper_right = (right_x, top_y)

    # 切り抜いたページを新しいPDFファイルに保存
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page)
    with open(output_name, 'wb') as new_pdf_file:
        pdf_writer.write(new_pdf_file)
'''
#PDFの画像から切り抜き、画像を保存する処理（現在のファイル名,出力ファイル名,Tmpファイル名,座標＊4）
def K_PDF(file_name,output_file,tmpfile,L_x,B_y,R_x,T_y):
    # PyPDF2を使用してページを切り抜く
    pdf_reader = PyPDF2.PdfReader(file_name)
    page = pdf_reader.pages[0]

    left_x = L_x  # 左上のx座標
    bottom_y =B_y  # 左上のy座標
    right_x =R_x  # 右下のx座標
    top_y =T_y  # 右下のy座標

    page.cropBox.lowerLeft = (left_x, bottom_y)
    page.cropBox.upperRight = (right_x, top_y)

    # 切り抜いたページを一時的なPDFファイルに保存
    temp_pdf_path = tmpfile
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page)
    with open(temp_pdf_path, 'wb') as temp_pdf_file:
        pdf_writer.write(temp_pdf_file)

    # 一時的なPDFファイルから画像を抽出
    images = convert_from_path(temp_pdf_path, first_page=1, last_page=1)
    if images:
        images[0].save(output_file, 'JPEG')

    # 一時的なPDFファイルを削除
    os.remove(temp_pdf_path)



def K_images(file_name):
    print("切り抜き")



def Kirinuki(file_name):
    print("切り抜き")
    #ファイルの拡張子を判断
    if('pdf'==file_extension(file_name)):
        print("PDF")
        #K_PDF(file_name,output_file,tmpfile,L_x,B_y,R_X,T_Y)
        #K_PDF(file_name,output_file,tmpfile,L_x,B_y,R_X,T_Y)
        #K_PDF(file_name,output_file,tmpfile,L_x,B_y,R_X,T_Y)
    else:
        print("images")
        K_images()
    









def DBSystem(OCR_data):
    print("DB")
        #ループ
            #PythonでSQL問い合わせ
            #問い合わせ結果をリストに格納にする
        #リストをjson形式に変換する json.loads(data)

    #return 結果のjson変数
 
def file_to_base64(file_path):  #不使用予定
    with open(file_path, "rb") as file:
        base64_data = base64.b64encode(file.read()).decode("utf-8")
        return base64_data
    
@app.route('/api/Kirinuki',methods=['POST'])#これはPOSTに変更しておく
def index():
    upload_file()
    
    



if __name__ == '__main__':
    app.run()
