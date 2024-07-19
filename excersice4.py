import random
import string
def word(a):
    if len(a)>3:
        print(a[1:] + a[0])
user_input = input("ennter the word for decoding:")
at_end = word(user_input)



