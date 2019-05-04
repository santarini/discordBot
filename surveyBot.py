import schedule
import time
import datetime
import random
import pyautogui

def job():
    #figure out what time it is and generate some random numbers
    #wait is done in terms of seconds
    timeNow = datetime.datetime.now().strftime("%H:%M:%S")
    random_num_1 = random.uniform(3,10)
    random_num_2 = random.uniform(1,10)

    pyautogui.typewrite("Hey fam do my survey: https://bit.ly/2ZU0mfE"
    time.sleep(random_num_1)
    pyautogui.typewrite("\n")
    
    
    pyautogui.typewrite("Trying to figure out what to call my web app")
    time.sleep(random_num_2)
    pyautogui.typewrite("\n")
    print("Completed: " + timeNow)



schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every(5).to(10).minutes.do(job)

while True:
    schedule.run_pending()
