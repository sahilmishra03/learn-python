import inspect


def info(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        print(func.__name__)
        print(inspect.signature(func))
    return wrapper

@info
def sum(a,b):
    return a+b

sum(6,7)