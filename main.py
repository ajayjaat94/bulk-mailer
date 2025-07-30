import streamlit as st
from Home import show_home
from SendEmails import show_email_sender

st.set_page_config(page_title="Mail Automation", layout="centered")

if "plan_selected" not in st.session_state:
    st.session_state.plan_selected = False

if not st.session_state.plan_selected:
    show_home()
else:
    show_email_sender()
