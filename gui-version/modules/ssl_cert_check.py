def analyze_cert(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    certs = [line for line in lines if "SSL" in line or "CERT" in line]
    return "Certificate-related entries:\n" + "\n".join(certs) if certs else None