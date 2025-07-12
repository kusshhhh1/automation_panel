import streamlit as st
from modules import email_sender, file_manager, network_tools, sys_monitor
st.set_page_config(page_title="Automation Panel", layout="wide")
st.title("⚙️ Enterprise Automation Panel")
st.sidebar.title("👋 Welcome Kushagra Sharma")

panel = st.sidebar.selectbox("Choose Module", [
    "📨 Email Sender", 
    "📁 File Manager", 
    "🖥️ System Monitor", 
    "🌐 Network Tools"
])

if panel == "📨 Email Sender":
    email_sender.send_email_ui()

elif panel == "🐳 Docker Manager":
    docker_manager.manage_docker_ui()

elif panel == "📁 File Manager":
    file_manager.file_manager_ui()

elif panel == "🖥️ System Monitor":
    sys_monitor.system_stats_ui()

elif panel == "🌐 Network Tools":
    network_tools.network_tools_ui()
