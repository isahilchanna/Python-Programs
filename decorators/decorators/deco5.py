def new_pretty(func):
    def new_inner():
        print("Hi, I got decorated")
        func()
    return new_inner

# decorating function
@new_pretty
def theNormal():
    print("Hi, I'm theNormal")

theNormal()

"""
Equivalent to
pret1 = new_pretty(theNormal)
pret1()
"""