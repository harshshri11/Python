def fib(n):
  if(n==0):
    return 0
  if(n==1):
    return 1
  else:
    return fib(n-1)+fib(n-2)
print(fib(9))

def sunat(n):
  if n==1:
   return 1
  return n + sunat(n-1)
print(sunat(6))

def power(num, pow):
 if pow == 0:
   return 1
 else:
   return num*power(num, pow-1)

print(power(2, 4))
