import datetime
import time


def current_time():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    print(current_time)
    print(f"현재시간은 {hour}시 {minute}분 {second}초 입니다")

current_time()
time.sleep(5)
current_time()
