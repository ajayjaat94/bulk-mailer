import streamlit as st
from utils.email_utils import send_bulk_emails
from utils.file_parser import extract_emails_from_file
import re

def show_email_sender():
    st.title('📧 Mail Automation Tool')

    st.header(f'Send Bulk Emails (Plan Limit: {st.session_state.MAX_EMAILS_ALLOWED} emails, {st.session_state.MAX_ATTACHMENT_SIZE_MB}MB attachments)')
    sender_email = st.text_input("Enter your Gmail ID")
    app_password = st.text_input("Enter your App Password", type="password")
    with st.expander("\u2139\ufe0f How to create an App Password for Gmail"):
        st.markdown("""
        **To create a Gmail App Password:**
        1. Visit your [Google Account Security Settings](https://myaccount.google.com/security).
        2. Turn on **2-Step Verification** if not already enabled.
        3. Scroll down to **App passwords**.
        4. Generate a new app password for "Mail".
        5. Copy and paste the generated 16-character password here.

        > \u2757 *App Passwords work only if 2-Step Verification is enabled on your Google account.*
        """)

    input_method = st.radio("Input email addresses from:", ["Paste Text", "Upload File"])
    email_list = []

    if input_method == "Paste Text":
        pasted = st.text_area("Paste email addresses (comma/newline separated)")
        if pasted:
            email_list = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", pasted)
    else:
        email_list = extract_emails_from_file(st.session_state.MAX_ATTACHMENT_SIZE_MB)

    if len(email_list) > st.session_state.MAX_EMAILS_ALLOWED:
        st.warning(f"⚠️ You selected {len(email_list)} emails. Only the first {st.session_state.MAX_EMAILS_ALLOWED} will be used.")
        email_list = email_list[:st.session_state.MAX_EMAILS_ALLOWED]

    if email_list:
        st.success(f"✅ {len(email_list)} valid email(s) found.")
        st.write(email_list)

    subject = st.text_input("Subject")
    message = st.text_area("Message (HTML supported)")
    attachments = st.file_uploader("Upload Attachments", accept_multiple_files=True)

    total_size_mb = sum(f.size for f in attachments) / (1024 * 1024)
    if total_size_mb > st.session_state.MAX_ATTACHMENT_SIZE_MB:
        st.error(f"❌ Total attachment size exceeds limit.")
        attachments = []

    if st.button("📤 Send Emails"):
        send_bulk_emails(sender_email, app_password, email_list, subject, message, attachments)
