#map
from functools import reduce
l = [2, 5, 6, 8, 55, 11, 10]
triple = list(map(lambda x: x*3, l))
print(triple)

#filiter
even = filter(lambda x: x%3 == 0, l)
print(list(even))

#reduce
sum = reduce(lambda x, y: x+y, l)
print(sum)