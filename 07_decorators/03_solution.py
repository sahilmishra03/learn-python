import time
def cache_memory(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args]=result
        return result
    return wrapper

@cache_memory
def sum(a,b):
    time.sleep(4)
    return a+b

print(sum(4,3))
print(sum(4,3))
print(sum(6,8))
print(sum(6,8))
print(sum(10,8))