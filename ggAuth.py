import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests

st.title("Title")

def ggAuth():
    
    # Google Authentication
    st.subheader("Google Authentication")
    client_id = "268734706774-ae6maqv35ag8dqbi3h77hhd3q14k77hn.apps.googleusercontent.com"
    token = st.text_input("Enter your Google ID token", type="password")
    if st.button("Authenticate"):
        if not token:  # Check if the token is empty
            st.warning("Please enter a valid Google ID token")
        elif not token.isdigit():  # Check if the token is a number
            st.error("Invalid Google ID token format. Please enter a valid token.")
        else:
            try:
                idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
                if idinfo['aud'] != client_id:
                    raise ValueError("Invalid client ID")
                st.success(f"Authentication successful: {idinfo['name']}")
            except ValueError as e:
                st.error("Authentication failed")
                st.error(e)
