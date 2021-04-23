# Tuples are like lists & dictionaries BUT they are IMMUTABLE!
# Once an element is inside a tuple, it CANNOT be reassigned
# Tuples use parenthesis

t = (1, 2, 3)
print(type(t))
# <class 'tuple'>

my_list = [1, 2, 3]
print(type(my_list))
# <class 'list'>

t = ('one', 2)

print(t)
# ('one', 2)

print(t[0])
# one

print(t[-1])
# 2

# INDEX METHOD
t = ('a', 'a', 'b')

print(t.index('a'))
# returns first index where the passed argument shows up in the tuple
# 0

print(t.index('b'))
# 2

# COUNT METHOD
print(t.count('a'))
# 2

# WHAT MAKES A TUPLE DIFFERENT (IMMUTABILITY)
print(my_list)
# [1, 2, 3]

my_list[0] = 'NEW'

print(my_list)
# ['NEW', 2, 3]

# t[0] = 'NEW'
# TypeError: 'tuple' object does not support item assignment


# WHY SHOULD I USE A TUPLE?
# Benefits: When passing around objects in your program and you don't want them to be changed.
