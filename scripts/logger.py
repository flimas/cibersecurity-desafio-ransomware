from datetime import datetime
import config

def log_action(action, details):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(config.LOG_FILE, "a") as log_file:
        log_file.write(f"{timestamp} - {action}: {details}\n")
        