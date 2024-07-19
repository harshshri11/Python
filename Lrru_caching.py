from functools import lru_cache
import time
@lru_cache(maxsize = None)
def sleep(m):
    time.sleep(5)
    return m
print(sleep(69))
print("done for 69")
print(sleep(68))
print("done for 68")
print(sleep(67))
print("done for 67")
print(sleep(69))
print("done for 69")
print(sleep(68))
print("done for 68")
print(sleep(67))
print("done for 67")
