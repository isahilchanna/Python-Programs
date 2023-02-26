# Example of returning a tuple-like object
import collections
player = collections.namedtuple("player", ["name", "age", "country"])

# objects of newtuple
p1 = player("Fred", 28, "Brazil")
p2 = player("Marcelo", 31, "Brazil")

print(p1.age)
print(p2.name, p2.age)
