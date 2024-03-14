import streamlit as st 
from streamlit_option_menu import option_menu

selected = option_menu (
    menu_title = None,
    options = ["Login","Chat bot","Payment"],
    default_index =0,
    orientation = "horizontal"
)
