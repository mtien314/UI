from threading import local
from matplotlib.backend_bases import cursors
import mysql.connector
import pandas as pd


def update_user_record(user_id,user_email):
    conn = mysql.connector.connect(host = "localhost",
                               port = "3306",
                               user = "root",
                               passwd = "123",
                               db = "doctor"
                               )


    cursor = conn.cursor()

#create user table

#cursor.execute("CREATE TABLE IF NOT EXISTS User (ID TEXT, Email TEXT)")
#update

    user_record = cursor.execute('SELECT * FROM User')
    result = cursor.fetchall()

    df = pd.DataFrame(result,columns = ['ID','Email'])
    if user_id not in df['ID']:
        if user_email not in df['Email']:
            cursor.execute('INSERT INTO User (ID,Email) VALUES (%s,%s);',
                       (user_id,user_email))
            conn.commit()
    cursor.close()
