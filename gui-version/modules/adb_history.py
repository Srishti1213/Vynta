def check_adb_commands(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        commands = [line.strip() for line in f.readlines()]
    risky = [cmd for cmd in commands if "shell" in cmd or "install" in cmd or "pull" in cmd]
    if risky:
        return "Suspicious ADB commands:\n" + "\n".join(risky)
    return None