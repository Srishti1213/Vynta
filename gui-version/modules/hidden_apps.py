def check_hidden_apps(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        packages = [line.strip() for line in f.readlines() if line.strip()]
    hidden = [pkg for pkg in packages if pkg.startswith('.') or 'com.android.' not in pkg]
    if hidden:
        return "Suspicious hidden apps found:\n" + "\n".join(hidden)
    return None