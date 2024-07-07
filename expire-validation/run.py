import datetime
import os

DATA_FILE = "program_data.dat"
LOG_FILE = "program_log.txt"

def read_last_access_time():
    try:
        with open(DATA_FILE, 'r') as file:
            last_access_str = file.readline().strip()
            timestamp_str = last_access_str.split(': ')[1]  # Extract timestamp part
            last_access_time = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
            return last_access_time
    except (FileNotFoundError, IndexError, ValueError):
        return None

def write_current_access_time():
    current_time = datetime.datetime.now()
    with open(DATA_FILE, 'w') as file:
        file.write(f"Installation Date: {current_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")

def log_access_time():
    current_time = datetime.datetime.now()
    log_entry = f"Program accessed at: {current_time}\n"
    with open(LOG_FILE, 'a') as file:
        file.write(log_entry)

# Read last access time
last_access_time = read_last_access_time()

if last_access_time:
    print(f"Last access time: {last_access_time}")
else:
    print("First time access or data file not found.")

# Write current access time
write_current_access_time()

# Log access time
log_access_time()
