# Building a simple generator function.
def newGenerator():
    print("First Result")
    yield 20

    

    print("Second Result")
    yield 40

    print("Last Result")
    yield 60

# return values for each yield
gen1 = newGenerator()
print(next(gen1)) 
#print(next(gen1)) 
print(next(gen1)) 

