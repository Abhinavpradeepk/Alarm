from tkinter import *
import datetime as dt
import time
import pygame
pygame.mixer.init()

def alarm(setAlarmtimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H:%M:%S")
        # currentDate = actualTime.strftime("%d/%m/%y")
        the_message = "currenttime: " + str(currentTime)
        print(the_message)
        if currentTime == setAlarmtimer:
            pygame.mixer.music.load("Desktop\hello\ws.SND_ASYNC\Sound.wav")
            pygame.mixer.music.play(loop=0)
           
            break
def getAlarmTime():
    alarmSetTime = f"{hour.get()}: {minute.get()}:{Second.get()}"
    alarm(alarmSetTime)


guiwindow = Tk()
guiwindow.title("THE ALARM CLOCK")
guiwindow.geometry("464x200")
guiwindow.config(bg = "#87BDD8")
guiwindow.resizable(width = True , height = True)

timeFormat = Label(
     guiwindow,
     text = "remember to set time format in 24-hour",
     fg="red",
     bg = "#36486A",  
     font = ("Arial", 17)
    ).place(
     x=0,
     y=160

    )
add_time = Label(
     guiwindow,
     text = "Hour    Minute    Second",
     font = 55,
     fg = "black",
     bg = "#87BDD8"  
    ).place(
      x=225,
      y=10

    )
setAlarm = Label(
      guiwindow,
      text = "set time for alarm",
      fg="white",
      bg = "#034F84",
      relief="solid",
      font = ("Helevetica", 13, "bold")  
    ).place(
     x=5,
     y=50

    )
test = Label(
    guiwindow,
    text = "testing...",
    fg="white",
    bg =  "#034F84",
    relief="solid",
    font =("Helevetica", 13, "bold")
    ).place(
        x=10,
        y=130

    )
hour = StringVar()
minute = StringVar()
Second = StringVar()
hourTime = Entry(
       guiwindow,
       textvariable=hour,
       bg = "#FEFBD8", 
      
       font = (20)  
    ).place(
        x=220,
        y=53

    )
minuteTime = Entry(  
    guiwindow,  
    textvariable = minute,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 297,  
        y = 53  
        )  
secondTime = Entry(  
    guiwindow,  
    textvariable = Second,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 390,  
        y = 53  
        )  

submit = Button(  
    guiwindow,
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#82B74B",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  
        x = 140,  
        y = 100  
        )  








guiwindow.mainloop()





