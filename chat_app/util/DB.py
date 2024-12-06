import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="chat_db_cn",
            db="chatapp",
            user="testuser",
            password="testuser",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
