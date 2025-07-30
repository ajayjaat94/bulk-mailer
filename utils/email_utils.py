import smtplib
from email.message import EmailMessage
import streamlit as st

def send_bulk_emails(sender_email, app_password, email_list, subject, message, attachments):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)

        sent_count = 0
        status = st.empty()

        for idx, recipient in enumerate(email_list, 1):
            msg = EmailMessage()
            msg["From"] = sender_email
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.set_content(message, subtype='html')
            for file in attachments:
                msg.add_attachment(file.read(), maintype="application", subtype="octet-stream", filename=file.name)
            try:
                server.send_message(msg)
                sent_count += 1
            except Exception as e:
                st.warning(f"Failed to send to {recipient}: {e}")
            status.info(f"Sent {sent_count} of {len(email_list)} emails...")

        server.quit()
        status.success(f"✅ All done! {sent_count} of {len(email_list)} emails sent successfully!")

    except Exception as e:
        st.error(f"❌ Error: {e}")
