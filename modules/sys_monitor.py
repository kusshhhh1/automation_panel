import streamlit as st
import psutil
import socket
import platform
import datetime
import os

def system_stats_ui():
    st.header("🖥️ System Monitor")

    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)
    st.metric(label="🧠 CPU Usage", value=f"{cpu_percent} %")

    # RAM Usage
    memory = psutil.virtual_memory()
    ram_used = memory.used // (1024 ** 2)
    ram_total = memory.total // (1024 ** 2)
    st.metric(label="💾 RAM Used", value=f"{ram_used} MB", delta=f"{memory.percent} %")

    # Disk Usage (auto-detect for all OS)
    disk = None
    partitions = psutil.disk_partitions()
    for p in partitions:
        try:
            if os.name == "nt" and 'cdrom' in p.opts.lower():
                continue  # Skip CD-ROMs on Windows
            disk = psutil.disk_usage(p.mountpoint)
            break
        except Exception:
            continue

    if disk:
        disk_used = disk.used // (1024 ** 3)
        disk_total = disk.total // (1024 ** 3)
        st.metric(label="💽 Disk Used", value=f"{disk_used} GB", delta=f"{disk.percent} %")
    else:
        st.error("Could not detect disk usage.")

    # Uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    st.metric(label="⏱️ System Uptime", value=str(uptime).split('.')[0])

    # IP Address
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "Unavailable"
    st.metric(label="🌐 IP Address", value=ip_address)

    # OS Info
    st.subheader("🖥️ OS Information")
    st.code(f"{platform.system()} {platform.release()} ({platform.version()})")
