import streamlit as st
import os
from modules import (
    hidden_apps, permission_audit, sms_call_log, file_audit, adb_history, gps_timeline,
    whois_lookup, dns_check, port_scanner, social_detector, email_validator,
    traceroute_map, protocol_detector, ssl_cert_check, bandwidth_analyzer
)

st.set_page_config(page_title="Android Forensic Suite", layout="centered")

st.title("📱 Android Analysis Web Interface")
st.write("Select a forensic tool and upload the corresponding log file:")

TOOLS = {
    "Hidden Apps Detection": ("sample_applist.txt", hidden_apps.check_hidden_apps),
    "Permission Audit": ("sample_permissions.txt", permission_audit.audit_permissions),
    "SMS & Call Logs": ("sample_sms_call_log.txt", sms_call_log.scan_sms_calls),
    "File System Audit": ("sample_filesystem.txt", file_audit.find_exfil_paths),
    "ADB History": ("sample_adb_log.txt", adb_history.check_adb_commands),
    "GPS Timeline": ("sample_location.csv", gps_timeline.extract_gps_movement),
    "WHOIS Lookup": ("sample_dns.txt", whois_lookup.check_domain_owner),
    "DNS Queries": ("sample_dns.txt", dns_check.resolve_dns),
    "Port Scanner": ("sample_portscan.txt", port_scanner.scan_ports),
    "Social Engineering Detection": ("sample_phishing_message.txt", social_detector.detect_social_engineering),
    "Email Header Validation": ("sample_email_headers.txt", email_validator.analyze_email_headers),
    "Traceroute Mapping": ("sample_traceroute.txt", traceroute_map.map_route),
    "Unusual Protocols": ("sample_protocol_log.txt", protocol_detector.detect_unusual_protocols),
    "SSL Certificate Inspection": ("sample_ssl_cert.txt", ssl_cert_check.analyze_cert),
    "Bandwidth Anomaly Detection": ("sample_bandwidth.csv", bandwidth_analyzer.detect_anomalies),
}

tool = st.selectbox("Choose Tool", list(TOOLS.keys()))
uploaded_file = st.file_uploader("Upload a log file", type=["txt", "csv"])

if uploaded_file is not None:
    input_path = os.path.join("samples", "uploaded_input")
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    st.write(f"✅ Running: {tool}")
    try:
        TOOLS[tool][1](input_path)
        st.success("Done!")
    except Exception as e:
        st.error(f"Error: {e}")
