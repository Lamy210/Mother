#SQL作成
import sqlite3

dbname = 'PfsallTextbook.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# テーブル作成のSQL文
create_table_sql = '''
CREATE TABLE IF NOT EXISTS textbook_list (
    textbook_number STRING,
    grade INTEGER,
    lecture_title STRING,
    professor STRING,
    book_title STRING,
    tvalue INTEGER
)
'''
cur.execute(create_table_sql)


select_data_sql = "SELECT * FROM textbook_list"
cur.execute(select_data_sql)
rows = cur.fetchall()
for row in rows:
    print(row)

# 接続を閉じる
conn.close()

