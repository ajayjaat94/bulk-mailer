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


page = st.sidebar.selectbox("Navigate", ["Home", "Privacy Policy", "Terms & Conditions", "Contact Us"])

if page == "Home":
    st.title("Welcome to Bulk Mailer")
    st.write("Send bulk emails easily and securely.")

elif page == "Privacy Policy":
    st.title("Privacy Policy")
    st.markdown("""
    We value your privacy. This app does not store any personal information beyond what is necessary to send emails. Data is not shared with third parties.
    """)

elif page == "Terms & Conditions":
    st.title("Terms and Conditions")
    st.markdown("""
    By using this service, you agree to use it responsibly and not for spamming or illegal purposes.
    """)

elif page == "Contact Us":
    st.title("Contact Us")
    st.markdown("""
    **Email:** theitexpert830@gmail.com
    **Phone:** +91-9462202210 
    **Address:** Narayan Tower, C-123 Moti Marg, Bapu Nagar, Jaipur, 
                 Rajasthan, India
    """)

