# Multiple decorators can be chained in Python
def starting(func):
    def inner(*args, **kwargs):
        print("-" * 35)
        func(*args, **kwargs)
        print("-" * 35)
    return inner

def astriskNew(func):
    def inner(*args, **kwargs):
        print("*" * 35)
        func(*args, **kwargs)
        print("*" * 35)
    return inner

@starting
@astriskNew
def displaying(txt):
    print(txt)

displaying("Python is so cool")