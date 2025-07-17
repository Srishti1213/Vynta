def detect_unusual_protocols(log_file):
    protocols = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if "proto=" in line:
                protocols.append(line.strip())
    return "Detected protocols:\n" + "\n".join(protocols) if protocols else None