import mysql.connector

conn = mysql.connector.connect(host='localhost',database='books',user='root',password='19910203')

if conn.is_connected():
    print("oh ya")
    conn.close()
else:
    print("oh no")
    conn.close()