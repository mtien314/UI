import streamlit as st
import webbrowser
import streamlit_google_oauth as oauth
from credentials import client_id, client_secret, redirect_uri
from streamlit_navigation_bar import st_navbar
import update
from user_record import update_user_record


url = 'https://buy.stripe.com/test_aEUaH5bhH7PP8nueUU'


swich_page = st.session_state.get("page_index",0)

def ggAuth():
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri
    )
    
    if login_info:
        user_id,user_email = login_info
        update_user_record(user_id,user_email)
        st.text(f"Welcome {user_email}")


if swich_page ==0:
    page = st_navbar(['Home','Subscription','Chat','Search','Solutions','Contact','Login'])

    if page == 'Subscription':
        webbrowser.open_new_tab(url)
        update.update_customers()
        update.update_transaction()



    if page =="Login":
        ggAuth()
        st.session_state["page_index"] = 1

if swich_page ==1:
    page = st_navbar(['Home','Subscription','Chat','Search','Solutions','Contact'])
    if page =='Home':
        st.write(f"Welcome")
        
