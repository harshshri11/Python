t = (3, 4, 6, 7, "harsh")
#print(t[-3])
list = list(t)
print(list)
t1 = (7, 6, 3, 8)
touple = t + t1
print(touple)
res = touple.count(7)
print("count of 7 is", res)
ind = touple.index(3, 6, 8)
print(ind)
if "harsh" in t:
    print("harsh is in touple")
