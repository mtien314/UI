from os import access
from more_itertools import last
from numpy import place
import streamlit as st
import webbrowser
import streamlit_google_oauth as oauth
from streamlit_navigation_bar import st_navbar
from time import sleep
import user_record
from user_record import update_user_record,update_account,check_account,find_accountID
import update
from st_pages import hide_pages

url = 'https://buy.stripe.com/test_aEUaH5bhH7PP8nueUU'



def ggAuth():

    info =  oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)
    if info:
        sleep(0.5) 
        user_id,user_email = info
        last_visited = 0
        update_user_record(user_id,user_email,last_visited)
        update_account(user_id,user_email)
        st.success("login success")
        st.switch_page("pages/page1.py")
    st.session_state.clear()


page = st_navbar(['Home','Subscription','Chat','Search','Solutions','Contact','Login'])
hide_pages(["page1"])


if page == 'Subscription':
    webbrowser.open_new_tab(url)

    #update customers and transaction

    update.update_customers()
    update.update_transaction()

if page =="Login":
    ggAuth()

    placeholder = st.empty()
    with placeholder.form("login"):
        st.markdown("### Login")

        email = st.text_input("Email")
        pasw = st.text_input("Password", type = "password")
            
        actual_pass = check_account(email)
        submit = st.form_submit_button("login")

    if pasw == actual_pass:
        st.success("Login success")

        user_id = find_accountID(email)
        update_user_record(user_id=user_id,user_email=email,last_visited=0)
            
        placeholder = st.empty()
        sleep(0.5)
        st.switch_page("pages/page1.py")
        
    elif pasw ==None or actual_pass ==None:
        st.warning("Please login")
    elif pasw!=actual_pass:
        st.warning("Password/Email incorrect")
        
