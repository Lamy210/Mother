from flask import Flask, render_template,request, jsonify,session
from werkzeug.utils import secure_filename
from pathlib import Path
from flask_cors import CORS
import secrets
import json

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # 16バイトのランダムな値を生成
def allowed_file(filename):
    # 受け入れる拡張子のリスト
    allowed_extensions = ['jpeg', 'pdf', 'jpg', 'png']
    # ファイルの拡張子を取得
    extension = filename.rsplit('.', 1)[1].lower()
    # 拡張子が許可されたリストに含まれているかチェック
    return '.' in filename and extension in allowed_extensions

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
def Kirinuki():
    print("切り抜き中")
    ##########################################
    #セッションの処理を追加する




    ###########################################

    ##############################
    #切り抜きの処理を実行する



    ################################




@app.route('/Kirinuki')
def index():
    upload_file()
    


        
    



if __name__ == '__main__':
    app.run()
