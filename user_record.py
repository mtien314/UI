import mysql.connector
import pandas as pd
from datetime import datetime



def connect(table):
    conn = mysql.connector.connect(host = "localhost",
                               port = "3306",
                               user = "root",
                               passwd = "123",
                               db = "doctor"
                                )
    cursor = conn.cursor()
    users = cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()
    cursor.close()
    return result


def update_user_record(user_id,user_email,last_visited):
    conn = mysql.connector.connect(host = "localhost",
                               port = "3306",
                               user = "root",
                               passwd = "123",
                               db = "doctor"
                               )


    cursor = conn.cursor()
    users = cursor.execute("SELECT * FROM User")
    result = cursor.fetchall()
    df = pd.DataFrame(result,columns =['ID','Email','Register','Last_visited'])

    mail = [str(x) for x in df['Email']]
    if user_email not in mail:
        register = datetime.now()
        cursor.execute('INSERT INTO User(ID, Email ,Register, Last_visited) VALUES (%s,%s,%s,%s);',
                   (user_id,user_email,register,last_visited))
        conn.commit()
    else:
        register = 0
        cursor.execute('INSERT INTO User(ID, Email ,Register, Last_visited) VALUES (%s,%s,%s,%s);',
                   (user_id,user_email,register,last_visited))
        conn.commit()
    cursor.close()



def update_account(user_id,user_email):
    conn = mysql.connector.connect(host = "localhost",
                               port = "3306",
                               user = "root",
                               passwd = "123",
                               db = "doctor"
                               )

    cursor = conn.cursor()

    users = cursor.execute('SELECT *FROM account')
    result = cursor.fetchall()
    df = pd.DataFrame(result,columns =['ID','Email','Password'])

    mail = [str(x) for x in df['Email']]
    if user_email not in mail:
        passw = 0
        cursor.execute('INSERT INTO account(ID, Email ,Password) VALUES (%s,%s,%s);',
                   (user_id,user_email,passw))
        conn.commit()
    cursor.close()

def update_account2(passw):
    conn = mysql.connector.connect(host = "localhost",
                               port = "3306",
                               user = "root",
                               passwd = "123",
                               db = "doctor"
                                )

    cursor = conn.cursor()
    sql = "UPDATE account SET Password=  %s WHERE Password = '0' LIMIT 1;"
    value = (passw,)
    cursor.execute(sql,value)
    conn.commit()
    cursor.close()


def check_account(email):
    result = connect(table = 'account')
    df = pd.DataFrame(result,columns =['ID','Email','Password'])
    
    mail = [x for x in df['Email']]
    if email in mail:
       actual_pass = df.loc[df['Email']==email,'Password'].values[0]
       return actual_pass
    else:
        return 0

def find_accountID(email):
    result = connect(table = 'account')
    df = pd.DataFrame(result,columns = ['ID','Email','Password'])
    mail = [x for x in df['Email']]
    account_ID = df.loc[df['Email']==email , 'ID' ].values[0]
    return account_ID


def history_logs(email,login_status):
    conn = mysql.connector.connect(host = "localhost",
                               port = "3306",
                               user = "root",
                               passwd = "123",
                               db = "doctor"
                                )
    cursor = conn.cursor()

    login = datetime.now()
    logout = "_"
    cursor.execute("INSERT INTO history_logs(Email, login, logout, login_status)"
                   "VALUES (%s, %s, %s, %s)",
                   (email, login, logout, login_status))
    conn.commit()
    cursor.close()
