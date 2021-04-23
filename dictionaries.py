# Dictionaries are unordered mappings for storing objects (cannot be sorted)
# Syntax:
# Use a dictionary when you don't need to know where something is in the dictionary

# Inserts key value pairs where ever in the object

my_dictionary = {'key1': 'value1', 'key2': 'value2'}
print(my_dictionary)
# {'key1': 'value1', 'key2': 'value2'}

print(my_dictionary['key1'])
# value1

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])
# 2.99


# Dict. are very flexible in the data they can hold
# Ex: lists and other dictionaries

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}

print(d['k2'])
# [0, 1, 2]

print(d['k3'])
# {'insideKey': 100}

print(d['k3']['insideKey'])
# 100

print(d['k2'][2])
# 2

d = {'key1': ['a', 'b','c']}

my_list = d['key1']

print(my_list)
# ['a', 'b', 'c']

letter = my_list[2]
print(letter)
# c

print(letter.upper())
# C


# IN ONE STEP
print(d['key1'][2].upper())
# C
