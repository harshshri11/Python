def func():
   try:
    a = int(input("enter the number:"))
    for i in range(1, 11):
     print(f"{a} * {i} = ",a*i)
    return 1
   except ValueError:
        print("invalid input")
        return 0
        #print("harsh")

   finally:
    print(" ")
if __name__ == "__main__":
    x = func()
    print(x)

