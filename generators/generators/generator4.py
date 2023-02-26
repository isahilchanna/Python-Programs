# short way to create a generator function using expression
# squared = (i * i for i in range(4))

# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))

# generator expression passed in a function
import math
print(sum(y * y for y in range(3)))