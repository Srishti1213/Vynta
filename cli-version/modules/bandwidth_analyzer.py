def detect_anomalies(log_file):
    spikes = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if "MB" in line or "GB" in line:
                spikes.append(line.strip())
    return "Bandwidth usage spikes:\n" + "\n".join(spikes) if spikes else None