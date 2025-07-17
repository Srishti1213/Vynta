def scan_ports(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        ports = [line.strip() for line in f if "open" in line.lower()]
    return f"Open ports found:\n" + "\n".join(ports) if ports else None