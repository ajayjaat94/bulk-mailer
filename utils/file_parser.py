import pandas as pd
import PyPDF2
import streamlit as st
import re

def extract_emails_from_file(max_size_mb):
    file = st.file_uploader("Upload Excel/CSV/PDF", type=["xlsx", "csv", "pdf"])
    email_list = []

    if file:
        if file.size > max_size_mb * 1024 * 1024:
            st.error(f"File size exceeds {max_size_mb} MB.")
        else:
            try:
                if file.name.endswith(".xlsx") or file.name.endswith(".xls"):
                    df = pd.read_excel(file)
                    email_list = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", df.to_string())
                elif file.name.endswith(".csv"):
                    df = pd.read_csv(file)
                    email_list = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", df.to_string())
                elif file.name.endswith(".pdf"):
                    reader = PyPDF2.PdfReader(file)
                    text = ''.join(page.extract_text() for page in reader.pages)
                    email_list = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
            except Exception as e:
                st.error(f"Error reading file: {e}")

    return email_list
