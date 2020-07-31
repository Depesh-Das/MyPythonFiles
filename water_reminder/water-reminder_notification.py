from datetime import datetime
from time import time
from plyer import notification

def notifyMe(title,message,icon):
    notification.notify(
        title=title,
        message=message,
        app_icon=icon,
        timeout=60,
    )

def log(msg):
    with open('my_log.txt','a') as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == "__main__":
    water_initial_time=time()
    eyeexercise_initial_time=time()

    water_time=30*60
    exercise_time=60*60

    while True:
        if time()-water_initial_time>water_time:
            notifyMe("Depesh","Water drinking time","water_QLz_icon.ico")
            timing=input("write save to entry the time the logs : ")
            if(timing=='save'):
                log("Drank water at")
                water_initial_time=time()
        if time()-eyeexercise_initial_time>exercise_time:
            notifyMe("Depesh","Eye exercise time","eye_rUc_icon.ico")
            timing=input("write save to entry the time the logs : ")
            if(timing=='save'):
                log("Eye exercise done at")
                eyeexercise_initial_time=time()