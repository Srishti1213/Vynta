def resolve_dns(log_file):
    domains = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if '.' in line:
                domains.append(line.strip())
    return f"Total domains found: {len(domains)}\n" + "\n".join(domains)