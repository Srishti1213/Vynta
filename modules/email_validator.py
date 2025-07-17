def analyze_email_headers(log_file):
    headers = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if "Received:" in line or "From:" in line:
                headers.append(line.strip())
    return "Parsed Email Headers:\n" + "\n".join(headers) if headers else None