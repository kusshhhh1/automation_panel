import streamlit as st
import socket
import subprocess

def network_tools_ui():
    st.header("🌐 Network Tools")

    host = st.text_input("🔍 Enter a Hostname or IP", value="google.com")

    # Ping tool
    if st.button("📡 Ping Host"):
        try:
            result = subprocess.run(["ping", "-n", "4", host], capture_output=True, text=True, shell=True)
            st.code(result.stdout)
        except Exception as e:
            st.error(f"Error: {e}")

    # IP lookup
    if st.button("🔎 Get IP Address"):
        try:
            ip = socket.gethostbyname(host)
            st.success(f"IP of {host}: {ip}")
        except Exception as e:
            st.error(f"Could not resolve IP: {e}")
