import schedule
import time
import datetime
import random
import pyautogui

def job():
    timeNow = datetime.datetime.now().strftime("%H:%M:%S")
    random_num_1 = random.uniform(3,10)
    random_num_2 = random.uniform(1,10)
    #wait is done in terms of seconds
    time.sleep(random_num_1)
    pyautogui.typewrite("Hey cunt faces do my survey: https://bit.ly/2ZU0mfE\n")
    time.sleep(random_num_2)
    pyautogui.typewrite("Trying to figure out what to call my web app\n")
    print("Completed: " + timeNow)


schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every(5).to(10).minutes.do(job)

while True:
    schedule.run_pending()
