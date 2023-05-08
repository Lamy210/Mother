from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
@app.route('/', methods=['POST'])
def upload_file():
    # リクエストからファイルを取得
    file = request.files['file']
    # ファイルを保存する場所を指定
    file.save('./test/' + file.filename)
    # レスポンスを返す
    return jsonify({'message': 'ファイルがアップロードされました'})

if __name__ == '__main__':
    app.run(debug=True)
