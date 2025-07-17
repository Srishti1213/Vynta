def check_domain_owner(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        domains = [line.strip() for line in f if line.strip()]
    return "WHOIS lookup not implemented in offline mode. Domains:\n" + "\n".join(domains)