def scan_sms_calls(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    calls = [line for line in lines if "CALL" in line.upper()]
    sms = [line for line in lines if "SMS" in line.upper()]
    return f"Calls Found: {len(calls)}\nSMS Found: {len(sms)}"