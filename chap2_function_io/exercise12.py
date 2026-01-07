import datetime
import time

def start_end_time(type_):
    if type_ == "start":
        print(f"START at {datetime.datetime.now()}")

    elif type_ == "end":
        print(f"END at {datetime.datetime.now()}")
    else:
        print("Warning Unknow type")

start_end_time("start")
time.sleep(45)
start_end_time('end')

