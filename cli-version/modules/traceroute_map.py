def map_route(log_file):
    hops = [line.strip() for line in open(log_file, 'r', encoding='utf-8') if line.strip()]
    return "Traceroute hops:\n" + "\n".join(hops) if hops else None