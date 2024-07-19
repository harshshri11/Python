import random
print("wellcome to snake, water, gun game!!")
def check(comp, user):
  if comp == user:
    return 0
  if (comp == 0 and user == 1):
   return -1

  if (comp == 1 and user == -1):
    return -1

  if (comp == -1 and user == 1):
    return -1

  return 1

while True:
  comp = random.randint(0, 2)
  user = int(input("enter '0' for snake, '1' for water, '2' for gun:\n"))
  score = check(comp,user)
  print("you: ",user)
  print("computer: ",comp)
  if(score == 0 ):
    print("its draw")
  elif (score == -1):
      print("you lose")
  else:
   print("you won")
   continue