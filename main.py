import streamlit as st
import os
import streamlit_google_oauth as oauth
from credentials import client_id, client_secret, redirect_uri
from streamlit_option_menu import option_menu
import webbrowser


def ggAuth():
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        selected = option_menu (
        menu_title = None,
        options = ['Chat bot 🤖','Payment 💸'],
        default_index =0,
        orientation = "horizontal"
    )
        st.write(f"Welcome {user_email}")
        if selected == "Payment":
            url = "https://buy.stripe.com/test_28o8Ay2a73Wg1ygeUU"
            webbrowser.open_new_tab(url)
        
login_info = ggAuth()
