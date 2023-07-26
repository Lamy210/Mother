import sqlite3
import csv

def search_and_export_data(search_string, filename):
    dbname = 'PfsallTextbook.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # データベースから特定の文字列を含むデータを取得して表示
    select_data_sql = f"SELECT * FROM textbook_list WHERE professor LIKE '%{search_string}%'"
    cur.execute(select_data_sql)
    rows = cur.fetchall()

    rows_sorted = sorted(rows, key=lambda x: (x[0] != '教科書番号', x[0]))  # 教科書番号でソートし、先頭行を固定

    with open(filename, 'a', newline='', encoding='utf-8-sig') as file:  # 追記モードでファイルを開く
        writer = csv.writer(file)
        # データ行の書き込み
        writer.writerows(rows_sorted)

    print(f"検索結果がファイルに追記されました: {search_string}")

    # 接続を閉じる
    conn.close()

# 入力された検索文字列とファイル名をリストとして取得
search_strings = input("検索する文字列を入力してください (複数の場合はカンマで区切ってください): ").split(',')
filename = input("結果を保存するCSVファイル名を入力してください: ")

# ヘッダー行の書き込み
header_row = ['教科書番号', '学年', '講義名', '担当教官', '書名', '本体価格']
with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(header_row)

# 各検索文字列に対して結果を追記
for search_string in search_strings:
    search_and_export_data(search_string.strip(), filename)

# ファイルの内容を読み込んで先頭行を固定
with open(filename, 'r', newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    rows = list(reader)
    rows_sorted = [header_row] + sorted(rows[1:], key=lambda x: x[0])

# ソートされた結果を上書き保存
with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerows(rows_sorted)

print("全ての検索結果がファイルに追記され、教科書番号ごとにソートされました:", filename)

#探索してそれをcsvファイルに変換する