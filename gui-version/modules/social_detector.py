def detect_social_engineering(log_file):
    suspicious_keywords = ['click here', 'urgent', 'verify', 'password', 'bank']
    alerts = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if any(kw in line.lower() for kw in suspicious_keywords):
                alerts.append(line.strip())
    if alerts:
        return "Social engineering indicators found:\n" + "\n".join(alerts)
    return None