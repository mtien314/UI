import numpy as np
import streamlit as st 
from streamlit_navigation_bar import st_navbar
from datetime import datetime
import mysql.connector
import pandas as pd
from time import sleep
from user_record import update_account2,connect

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



if page2 =="Logout":

    current_datetime = datetime.now()
    # Format the datetime object (replace with your preferred format)
    last_visited = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    update_lastime(last_visited)
    st.session_state.clear()
    st.switch_page("testUI.py")

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

    if pd.isnull(regist)==False and passw =='0':
        placeholder = st.empty()
     
        with placeholder.form("Change password"):
            st.markdown("### Change password")
            new_pass = st.text_input("New password", type = "password")
            pasw = st.text_input("Enter password again", type = "password")
            submit = st.form_submit_button("submit")
        if submit and new_pass != pasw:
            st.warning("Please check new_pass and pass again")
        if submit and new_pass ==pasw:
            st.success("Change password success")
            sleep(0.5)
            update_account2(new_pass)
            placeholder.empty()

    if passw !='0':
        st.write('Welcome')
