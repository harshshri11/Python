print("wellcome to koun banega carorpati")
question = ["1)what is the capital of austrlia", "a)sydeny b)lundon c)delhi d)mumbai", "2)population of india" ,"a)145cr b)150cr c)130cr d)123cr","3)who is pravin tambe","a)cricketer b)football player" "c)politetion d)president","4)india won world cup in which year", "a)1947 b) 1981 c)1993 d)2019"]
levels = [0,1000,2000,3000,4000]
money = 0
for item in levels(0,len(question)):
    print("quetion for rs{levels[i+1")
    print("{question[i][0]}")
    print(f"a. {question[i][1]} b. {question[i][2]}")
    print(f"a. {question[i][3]} b. {question[i][4]}")
reply = int(input("enter your answer here use small case letter"))
if i == 0:
    money=320000
if reply == question[i][-1]:
    print(f"\nyou've won rs {levels[i + 1]} ")
else:
 print("you have lost the game")
 print(f"\n\n your take home money is {money}")


