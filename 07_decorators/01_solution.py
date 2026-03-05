import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print("Total-Time",start-end)
        return result
    return wrapper

@timer
def helper(n):
    time.sleep(n)

helper(4)