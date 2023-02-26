def newIncrementing(a):
    return a + 1

def newDecrementing(a):
    return a - 1

def operating(func, a):
    result = func(a)
    return result

print(operating(newIncrementing, 3)) # 4
print(operating(newDecrementing, 3)) # 2
