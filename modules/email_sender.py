import streamlit as st
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load .env credentials
load_dotenv()

# Function to send email using smtplib
def send_email(to_email, subject, message):
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

# Streamlit UI function
def send_email_ui():
    st.header("📨 Send an Email")

    to_email = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")

    if st.button("Send Email"):
        if not to_email or not subject or not message:
            st.warning("Please fill in all fields.")
        else:
            try:
                send_email(to_email, subject, message)
                st.success("✅ Email sent successfully!")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
