import streamlit as st
import webbrowser
import streamlit_google_oauth as oauth
from credentials import client_id, client_secret, redirect_uri
from streamlit_navigation_bar import st_navbar


url = 'https://buy.stripe.com/test_aEUaH5bhH7PP8nueUU'



def ggAuth():
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        st.write(f"Welcome {user_email}")
    


page = st_navbar(['Home','Subscription','Chat','Search','Solutions','Contact','Login'])

if page == 'Subscription':
    webbrowser(url)


if page =="Login":
    ggAuth()
