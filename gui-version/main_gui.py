import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import os

# Import your analysis modules
from modules import (
    hidden_apps, permission_audit, sms_call_log, file_audit, adb_history, gps_timeline,
    whois_lookup, dns_check, port_scanner, social_detector, email_validator,
    traceroute_map, protocol_detector, ssl_cert_check, bandwidth_analyzer
)

# Map tool names to corresponding functions
TOOLS = {
    "Hidden Apps Detection": hidden_apps.check_hidden_apps,
    "Permission Audit": permission_audit.audit_permissions,
    "SMS & Call Logs": sms_call_log.scan_sms_calls,
    "File System Audit": file_audit.find_exfil_paths,
    "ADB History": adb_history.check_adb_commands,
    "GPS Timeline": gps_timeline.extract_gps_movement,
    "WHOIS Lookup": whois_lookup.check_domain_owner,
    "DNS Queries": dns_check.resolve_dns,
    "Port Scanner": port_scanner.scan_ports,
    "Social Engineering Detection": social_detector.detect_social_engineering,
    "Email Header Validation": email_validator.analyze_email_headers,
    "Traceroute Mapping": traceroute_map.map_route,
    "Unusual Protocol Detection": protocol_detector.detect_unusual_protocols,
    "SSL Certificate Inspection": ssl_cert_check.analyze_cert,
    "Bandwidth Anomaly Detection": bandwidth_analyzer.detect_anomalies,
}

def run_tool():
    tool = tool_choice.get()
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    output_text.delete('1.0', tk.END)
    try:
        result = TOOLS[tool](file_path)  # Capture and show output
        if result:
            output_text.insert(tk.END, f"✅ {tool} Results:\n{result}\n")
        else:
            output_text.insert(tk.END, f"✅ {tool} completed. No significant findings.\n")
    except Exception as e:
        output_text.insert(tk.END, f"❌ Error running {tool}:\n{str(e)}\n")

# GUI setup
root = tk.Tk()
root.title("Vynta - Android Forensic Suite")

frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text="Select a Forensic Tool:").grid(column=0, row=0, sticky=tk.W)

tool_choice = ttk.Combobox(frame, values=list(TOOLS.keys()), width=45)
tool_choice.grid(column=0, row=1)
tool_choice.set("Hidden Apps Detection")

ttk.Button(frame, text="Choose Log File & Run", command=run_tool).grid(column=0, row=2, pady=10)

output_text = scrolledtext.ScrolledText(frame, width=90, height=25)
output_text.grid(column=0, row=3, pady=5)

root.mainloop()
