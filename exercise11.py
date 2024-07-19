import time
import winsound
import win32com.client
from plyer import notification

def anhour(title, message):
    while True:
        notification.notify(
            title = title,
            message = message,
            timeout = 5
        )
        reminder_by_sound = ["hey Harsh its time to drink water"]
        reminder = win32com.client.Dispatch("SAPI.SpVoice")
        reminder.Speak(reminder_by_sound)
        time.sleep(1)
        winsound.Beep(2500, 1000)
        time.sleep(3600)
if __name__ == "__main__":
    reminder_title = "REMINDER!!"
    reminder_message = "Time to drink water!!!"
    anhour(reminder_title, reminder_message)


