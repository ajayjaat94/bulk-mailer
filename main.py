import streamlit as st
from Home import show_home
from SendEmails import show_email_sender

st.set_page_config(page_title="Mail Automation", layout="centered")

# Sidebar Navigation
st.sidebar.markdown("[Home](/?page=home)")
st.sidebar.markdown("[Privacy Policy](/?page=privacy-policy)")
st.sidebar.markdown("[Terms & Conditions](/?page=terms-and-conditions)")
st.sidebar.markdown("[Contact Us](/?page=contact-us)")
st.sidebar.markdown("[Cancellations & Refunds](/?page=refund-policy)")
st.sidebar.markdown("[Shipping Policy](/?page=shipping-policy)")

# Read query params
page = st.query_params.get("page", "home")

# Session state for app logic
if "plan_selected" not in st.session_state:
    st.session_state.plan_selected = False

# Route pages
if page == "home":
    if not st.session_state.plan_selected:
        show_home()
    else:
        show_email_sender()

elif page == "privacy-policy":
    st.title("Privacy Policy")
    st.markdown("""
    We value your privacy. This app does not store any personal information beyond what is necessary to send emails.  
    - We do not sell, trade, or rent your personal information.  
    - Any data used (like email addresses) is strictly for the purpose of sending emails as instructed by the user.  
    - We do not store the content of emails permanently.
    """)

elif page == "terms-and-conditions":
    st.title("Terms and Conditions")
    st.markdown("""
    By using Bulk Mailer, you agree to:  
    - Use this tool only for legal and non-spam email campaigns.  
    - Not misuse the platform for phishing, fraud, or illegal activity.  
    - We reserve the right to block or suspend accounts that violate our policies without prior notice.
    """)

elif page == "contact-us":
    st.title("Contact Us")
    st.markdown("""
    **Email:** theitexpert830@gmail.com  
    **Phone:** +91-9462202210  
    **Address:** Narayan Tower, C-123 Moti Marg, Bapu Nagar, Jaipur, Rajasthan, India
    """)

elif page == "refund-policy":
    st.title("Cancellations and Refunds")
    st.markdown("""
    We offer a digital service (email sending tool), and hence, we follow a strict no-refund policy.  
    - Subscriptions once purchased cannot be canceled or refunded.  
    - If you experience technical issues, please contact support and we will work to resolve them as quickly as possible.
    """)

elif page == "shipping-policy":
    st.title("Shipping Policy")
    st.markdown("""
    Our product is a digital service (email automation) and does not involve any physical shipping.  
    - Access to the platform is granted instantly upon successful payment and account activation.
    """)
