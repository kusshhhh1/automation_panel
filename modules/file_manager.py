import streamlit as st
import os

UPLOAD_DIR = "uploads"

def file_manager_ui():
    st.header("📁 File Manager")

    # Upload Section
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    # Show existing files
    st.subheader("📂 Uploaded Files")
    files = os.listdir(UPLOAD_DIR)

    if not files:
        st.info("No files found.")
    else:
        for file in files:
            st.write(f"📄 {file}")
            col1, col2 = st.columns(2)
            with col1:
                with open(os.path.join(UPLOAD_DIR, file), "rb") as f:
                    st.download_button(f"⬇️ Download {file}", f, file_name=file)
            with col2:
                if st.button(f"🗑️ Delete {file}"):
                    os.remove(os.path.join(UPLOAD_DIR, file))
                    st.warning(f"{file} deleted.")
                    st.experimental_rerun()
