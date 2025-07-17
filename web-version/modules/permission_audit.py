def audit_permissions(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        data = f.read()
    risky = [line for line in data.splitlines() if "android.permission" in line and any(word in line.lower() for word in ["sms", "call", "camera", "location"])]
    if risky:
        return "Risky permissions found:\n" + "\n".join(risky)
    return None