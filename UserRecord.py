import streamlit as st
import webbrowser
import streamlit_google_oauth as oauth
import sqlite3
from credentials import client_id, client_secret, redirect_uri
from streamlit_navigation_bar import st_navbar


def create_or_update_user(user_id, user_email):
    conn = sqlite3.connect(name_database)
    cursor = conn.cursor()
    
    # Check if the user exists in the database
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        # Update user's email if it has changed
        if existing_user[1] != user_email:
            cursor.execute("UPDATE users SET email=? WHERE user_id=?", (user_email, user_id))
            st.text("Your email was updated.")
        else:
            st.text("Your account already exists.")
    else:
        # Insert a new user record into the database
        cursor.execute("INSERT INTO users (user_id, email) VALUES (?, ?)", (user_id, user_email))
        st.text("Welcome new user!")
    
    conn.commit()
    conn.close()
