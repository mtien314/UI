import streamlit as st 
from streamlit_option_menu import option_menu

st.title('Title')
selected = option_menu (
    menu_title = None,
    options = ["Login","Chatbot","Payment"],
    icons = ['bi-info-square','robot','credit-card'],
    menu_icon="cast",
    default_index =0,
    orientation = "horizontal",
)
