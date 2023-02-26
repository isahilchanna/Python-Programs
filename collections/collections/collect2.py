# Example to remember the order of the keys
import collections

firstD = collections.OrderedDict()
firstD["X:"] = 70
firstD["Y:"] = 75
firstD["E:"] = 77
firstD["M:"] = 79

for k,v in firstD.items():
    print(k,v)
