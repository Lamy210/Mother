from flask import Flask, redirect, url_for, session, request
from oauthlib.oauth2 import WebApplicationClient
from urllib.parse import urlencode
import requests
import logging

app = Flask(__name__)
app.debug = True
app.secret_key = "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"

# クライアントIDとクライアントシークレットを設定します
client_id = "-2299155810-1mhkf2k3180vp14v8h6osq618jsr2g58.apps.googleusercontent.com"
client_secret = "-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"
redirect_uri = "https://127.0.0.1:5000/callback"

# Google OAuth 2.0クライアントを作成します
client = WebApplicationClient(client_id)

@app.route("/index", methods=["GET"])
def index():
    return "Hello, World!"

@app.route("/login",methods=['GET'])
def login():
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "openid email profile",
    }
    auth_url = "https://accounts.google.com/o/oauth2/auth?" + urlencode(params)
    return redirect(auth_url)

@app.route("/callback")
def callback():
    # Googleからのコールバックを処理し、アクセストークンを取得します
    token_url, headers, body = client.prepare_token_request(
        "https://accounts.google.com/o/oauth2/token",
        authorization_response=request.url,
        redirect_url=redirect_uri
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(client_id, client_secret)
    )
    client.parse_request_body_response(token_response.text)
    session["token"] = client.token

    # アクセストークンを使用してユーザーの情報を取得し、oecu.jpのドメインを持つか確認します
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    userinfo_response = requests.get(userinfo_url, headers={"Authorization": f"Bearer {client.token['access_token']}"})
    userinfo = userinfo_response.json()
    if "oecu.jp" in userinfo["email"]:
        # oecu.jpのドメインを持つアカウントのみを許可し、ログイン処理を実行します
        # ログイン後の処理やセッション管理などはアプリケーションに応じて行ってください
        logging.info("ログイン成功")
        return "ログイン成功！"
    else:
        # oecu.jpのドメインを持たないアカウントは拒否します
        logging.info("ログイン失敗")
        return "ログインに失敗しました。"

if __name__ == "__main__":
    app.debug=True
    app.run(ssl_context=("./cert.pem", "./key.pem"))
    #app.run()
    
