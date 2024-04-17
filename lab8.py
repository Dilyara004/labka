from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    log_level: str
    message: str

def parse_log_entry(line):
    parts = line.strip().split(" ", 2)
    if len(parts) != 3:
        raise ValueError("Invalid log entry format")
    timestamp = datetime.strptime(parts[0], "%Y-%m-%d")
    return LogEntry(timestamp, parts[1], parts[2])

def read_log_file(file_path):
    log_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            log_entries.append(parse_log_entry(line.strip()))
    return log_entries

def filter_logs_by_level(log_entries, level):
    return tuple(entry for entry in log_entries if entry.log_level == level)

def main():
    log_entries = read_log_file("main.log")
    error_logs = filter_logs_by_level(log_entries, "ERROR")
    print("Error logs:")
    for i, log in enumerate(error_logs, 1):
        print(f"{i}. {log.timestamp} {log.log_level}: {log.message}")

if __name__ == "__main__":
    main()
