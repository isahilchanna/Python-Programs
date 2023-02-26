# Using generator with For Loop
def upTo(i):
    for x in range(i):
        yield x


# get a sequence up to 
newSeq = upTo(4)

print(next(newSeq)) # 0
print(next(newSeq)) # 1
print(next(newSeq)) # 2
print(next(newSeq)) # 3
print(next(newSeq)) # StopIteration