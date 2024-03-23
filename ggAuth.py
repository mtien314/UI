import streamlit as st
import os
import streamlit_google_oauth as oauth
from credentials import client_id, client_secret, redirect_uri

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


login_info = ggAuth()
if login_info:
    user_id, user_email = login_info
    st.write(f"Welcome {user_email}")