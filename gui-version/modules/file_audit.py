def find_exfil_paths(log_file):
    suspicious_paths = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if any(x in line.lower() for x in ['upload', 'ftp', 'http', 'cloud', 'exfil']):
                suspicious_paths.append(line.strip())
    if suspicious_paths:
        return "Possible data exfiltration paths:\n" + "\n".join(suspicious_paths)
    return None