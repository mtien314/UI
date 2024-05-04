import numpy as np
import streamlit as st 
from streamlit_navigation_bar import st_navbar
from datetime import datetime
import mysql.connector
import pandas as pd
from time import sleep
import user_record
from user_record import update_account2,connect
import bcrypt
import webbrowser
import update

url = 'https://buy.stripe.com/test_aEUaH5bhH7PP8nueUU'

page2 = st_navbar(['Home','Subscription','Chat','Search','Solutions','Contact','Logout'])

def update_lastime(last_visited):
   
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
    n = len(df['Last_visited'])
    id = df['ID'][n-1]
    regist = df['Register'][n-1]
    
    if pd.isnull(regist)==True:
        sql = "UPDATE User SET Last_visited =  %s WHERE id = %s AND Register =0  AND Last_visited =0 LIMIT 1;"
        values = (last_visited,id)
        cursor.execute(sql,values)
        conn.commit()
    
    cursor.close()


def update_logout(last):
   
    conn = mysql.connector.connect(host = "localhost",
                               port = "3306",
                               user = "root",
                               passwd = "123",
                               db = "doctor"
                                )
    cursor = conn.cursor()
    users = cursor.execute("SELECT * FROM history_logs")
    result = cursor.fetchall()
    df = pd.DataFrame(result,columns =['Email', 'Login', 'Logout', 'Login_status'])
    n = len(df['Email'])
    email = df['Email'][n-1]
    logout = df['Logout'][n-1]
    log_status = df['Login_status'][n-1]

    if logout =='_':
        sql = "UPDATE History_logs SET logout = %s WHERE Email = email ORDER BY Login DESC LIMIT 1;"
        values = (last,)
        cursor.execute(sql,values)
        conn.commit()

    status = "Logged Out"
    if log_status =='Logged In':
        sql = "UPDATE History_logs SET Login_status = %s WHERE Email = email ORDER BY Login DESC LIMIT 1;"
        values = (status,)
        cursor.execute(sql,values)
        conn.commit()

    cursor.close()

if page2 =="Logout":

    current_datetime = datetime.now()
    # Format the datetime object (replace with your preferred format)
    last_visited = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    update_logout(last_visited)
    update_lastime(last_visited)
    st.session_state.clear()
    st.switch_page("main.py")

if page2 == 'Home':

    #update password
    result = connect(table ='User')
    df = pd.DataFrame(result,columns =['ID','Email','Register','Last_visited'])
    n = len(df['Last_visited'])
    id = df['ID'][n-1]
    regist = df['Register'][n-1]

    result2 = connect(table = 'account')
    df2 = pd.DataFrame(result2,columns =['ID','Email','Password'])
    n2 = len(df2['ID'])
    passw = df2['Password'][n2-1]

    if pd.isnull(regist)== False and passw =='0':
        placeholder = st.empty()
     
        with placeholder.form("Change password"):
            st.markdown("### Change password")
            new_pass = st.text_input("New password", type = "password")
            password = st.text_input("Enter password again", type = "password")
            submit = st.form_submit_button("submit")

            hash_passw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        if submit and new_pass != password:
            st.warning("Please check new_pass and pass again")
        if submit and new_pass == password:
            st.success("Change password success")
            sleep(0.5)
            update_account2(hash_passw)
            placeholder.empty()

    if passw !='0':
        st.write('Welcome')


    
if page2 =='Subscription':
    webbrowser.open_new_tab(url)

    #update customers and transaction

    update.update_customers()
    update.update_transaction()
