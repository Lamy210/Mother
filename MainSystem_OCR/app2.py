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
import uuid
from PIL import Image
import pytesseract

app = Flask(__name__)
CORS(app)
app.secret_key = secrets.token_hex(16)  # 16バイトのランダムな値を生成
def allowed_file(filename):
    # 受け入れる拡張子のリスト
    allowed_extensions = ['jpeg', 'pdf', 'jpg', 'png']
    # ファイルの拡張子を取得
    extension = filename.rsplit('.', 1)[1].lower()
    # 拡張子が許可されたリストに含まれているかチェック
    return '.' in filename and extension in allowed_extensions
def file_extension(file):
    print(str(file))
   # file_name =file.filename


    directory_path = "./test/"

    # ファイルパスからファイル名部分を取得
    file_name = os.path.basename(file)

    # 元のファイルパスからファイル名部分を取り除く
    new_file_path = file.replace(file_name, "")

    print(new_file_path)


    exten = file.split(".")[-1]

    return str(exten)
def get_extension_from_file_path(file_path):
    last_dot_index = file_path.rfind('.')
    if last_dot_index == -1:
        return ""  # ドットが見つからない場合は空の拡張子を返す
    return file_path[last_dot_index:]


def upload_file(Userid):
    # リクエストからファイルを取得
    file = request.files['file']
    if file and allowed_file(file.filename):
        # ファイルを保存する場所を指定
        save_path='./test/' + secure_filename(file.filename)
        file.save(save_path)

        print("39"+save_path)
        extension = get_extension_from_file_path(save_path)
        print(extension)

        #extension=file_extension(str(file))

        new_path='./test/'+str(Userid)+extension
        os.rename(save_path,new_path)
        print("upload_file:savepath"+new_path+"Userid:"+str(Userid))
        return new_path
    else:
        return -1
        # レスポンスを返す
        #return jsonify({'Message': 'ファイルがアップロードされました: [' + str(file) + ']'})
    #else:
       # return jsonify({'Error': '対象外のファイル形式かもしれえんから確認してほしい'})
    
def images(imagefile):
    image = Image.open(imagefile)

    # 画像からテキストを抽出（日本語と英語）
    text = pytesseract.image_to_string(image, lang='jpn+eng')

    # 抽出されたテキストを表示
    print(text)
#PDFの画像から切り抜き、画像を保存する処理（現在のファイル名,出力ファイル名,Tmpファイル名,座標＊4）
def K_PDF(file_name,output_file,tmpfile,L_x,B_y,R_x,T_y):
    # PyPDF2を使用してページを切り抜く
    pdf_reader = PyPDF2.PdfReader(file_name)
    page = pdf_reader.pages[0]

    page.cropbox.lower_left = (L_x,B_y)
    page.cropbox.upper_right = (R_x, T_y)

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



def K_images(file_name, output_file, L_x, B_y, R_x, T_y):
    # 画像を開く
    image = Image.open(file_name)
    # 画像を切り抜く
    cropped_image = image.crop((L_x, B_y, R_x, T_y))

    # 切り抜いた画像をJPEGファイルとして保存
    cropped_image.save(output_file, 'JPEG')


def Transform(file_name,uuid_v1):
    print("切り抜き")
    #ファイルの拡張子を判断
    output1="./test/"+str(uuid_v1)+"zenki.jpeg"
    output2="./test/"+str(uuid_v1)+"kouki.jpeg"
    output3="./test/"+str(uuid_v1)+"gakunen.jpeg"
    tempfile="./test/"+str(uuid_v1)+"tmp.pdf"
    
    print("139:"+file_name)
    if('pdf'==str(file_extension(str(file_name)))):
        print("PDF")
        #381*279
        K_PDF(file_name,output1,tempfile,260,140,570,710)#前期
        K_PDF(file_name,output2,tempfile,580,140,980,710)#後期
        K_PDF(file_name,output3,tempfile,20,710,26,720)#学年
    else:
        print("images")
        K_images(file_name,output1,L_x,B_y,R_X,T_Y)#前期
        K_images(file_name,output2,L_x,B_y,R_X,T_Y)#後期
        K_images(file_name,output3,L_x,B_y,R_X,T_Y)#学年
    
def DBSystem(OCR_data): 
    print("DB")
        #ループ
            #PythonでSQL問い合わせ
            #問い合わせ結果をリストに格納にする
        #リストをjson形式に変換する json.loads(data)

    #return 結果のjson変数
@app.route('/api/Kirinuki',methods=['POST'])#これはPOSTに変更しておく
def OutputssendProc():
    print("開始")    
    print("uuid")
    uuid_v1 = uuid.uuid1()
    print("uuid created")
    file_name=upload_file(uuid_v1)
    print("file_name:"+file_name)
    print("File")
    #return response
    if(file_name!=-1):
        Transform(file_name,uuid_v1)#添え字　ファイル名,UUID
        # 画像を開く
        image1=str(uuid_v1)+"zenki.jpeg"
        image2=str(uuid_v1)+"kouki.jpeg"
        image3=str(uuid_v1)+"gakunen.jpeg"
        images(image1)
        images(image2)
        images(image3)
    print("OK")

    

if __name__ == '__main__':
    app.run()#app.run(debug=True))
