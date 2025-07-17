def extract_gps_movement(log_file):
    coords = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if ',' in line and any(c.isdigit() for c in line):
                coords.append(line.strip())
    if coords:
        return "Extracted GPS coordinates:\n" + "\n".join(coords)
    return None