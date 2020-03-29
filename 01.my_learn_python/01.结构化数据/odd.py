from datetime import datetime
import time
import random

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,
        33,35,37,39,41,43,45,47,49,51,53,55,57,59]

#用range(5)，循环5次
for i in range(5):
    right_time = datetime.today().minute
    if right_time in odds:
        print("在这里")
    else:
        print("不在这里")
    time.sleep(random.randint(1,6))
