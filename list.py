list = [1,3,7,4,"harsh"]
print(list[0])
print(list[:])
print(list[len(list)-3])
if 71 in list:
    print("7 is present in list")

list1 = [i*i for i in range(10) if i % 2 == 0]
print(list1)