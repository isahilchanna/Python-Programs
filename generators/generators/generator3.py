# Yielding the square of a number
def squaredSequence(i):
    for x in range(i):
        yield x * x


newGenera = squaredSequence(6)
# while True:
#     try:
#         print("Received on next(): ", next(newGenera))
#     except StopIteration:
#         break
for square in newGenera:
    print(square)
