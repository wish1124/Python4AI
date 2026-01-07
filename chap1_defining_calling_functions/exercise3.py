import datetime
import time

def log_start_time():
    print(f"Start at {datetime.datetime.now()}")

def log_end_time():
    print(f"End at {datetime.datetime.now()}")


log_start_time()
time.sleep((5))
log_end_time()

