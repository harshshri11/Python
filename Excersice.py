import time
timedstamp = (time.strftime('%H:%M:%S'))
print(timedstamp)
n = input("enter your name")
hour = int(time.strftime('%H'))
print("hi", n, "current time is", timedstamp)
if 5 <= hour < 12:
    print("good morning ", n)
    if 12 <= hour < 16:
        print("good afternoon", n)
        if 5 <= hour < 24:
            print("good night")
