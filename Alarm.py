import datetime
from playsound import playsound
alarmhour=int(input("Enter hour:"))
alarmminute=int(input("Enter Minutes:"))
alarmAm=input("am /pm: ")

if alarmAm=="pm":
    alarmhour+=12
while True:
    if alarmhour==datetime.datetime.now().hour and alarmminute==datetime.datetime.now().minute:
        print("Playing...")
        playsound("alarm.wav")
        break
                    



