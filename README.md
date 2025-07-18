# Vynta: AI-Enriched Android Forensic Suite

**Author:** Srishti Yadav  

presentation
https://1drv.ms/p/c/403878e88d413891/EZeHMw-91W9EmBK8OZ8_7xABMC2ZOj0CctmkfkPuKPjyoA?e=xR4XL5
sample case : https://github.com/Srishti1213/vynta_sample_case
## 🔍 Overview

**Vynta** is a modular, AI-assisted forensic toolkit designed to detect internal data leaks, suspicious behavior, and malicious applications on **Android devices**. It leverages both **traditional forensic analysis** and **OSINT techniques** to deliver a comprehensive investigation framework for professionals, researchers, and law enforcement.

Vynta supports:
- 📁 Log-based forensic analysis
- 🌐 WHOIS, DNS, Traceroute, and SSL inspection
- 🧠 Detection of hidden apps, suspicious permissions, and exfiltration activity
- 🧪 15 core forensic modules
- 🧰 CLI, GUI (Tkinter), and Web (Streamlit) interfaces

---

## 📦 Features

- Hidden App Detection  
- Dangerous Permissions Audit  
- SMS and Call Log Scraping  
- File System Audit for exfiltration paths  
- ADB Command History Analysis  
- GPS Movement Timeline  
- WHOIS Lookup  
- DNS Query Tracking  
- Port Scan Data Analysis  
- Social Engineering Pattern Detection  
- Email Header Validation (SPF, DKIM, DMARC)  
- Traceroute Path Mapping  
- Unusual Protocol Detection (e.g., IRC, FTP)  
- SSL Certificate Inspection  
- Bandwidth Anomaly Detection

---

## 🖥️ Interface Options

You can run Vynta using one of three modes:

### 1. Web Interface (Streamlit)
```bash
python launch_suite.py
# Then choose: 1 - Streamlit Web Interface
