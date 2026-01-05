def parse_logs(log_text):
    lines = log_text.split("\n")
    error_lines = []

    for line in lines:
        if "error" in line.lower() or "failed" in line.lower():
            error_lines.append(line)

    return error_lines
