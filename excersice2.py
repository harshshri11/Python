import time

t = time.strftime('%H:%M:%S')
print("current time is",t)
hour = int(time.strftime('%H'))
print(hour)
if(hour>0 and hour<12):
    print("good morning")
elif(hour<=12 and hour>17):
    print("good aftrnoon")
if(hour>17 and hour<0):
    print("good night")
