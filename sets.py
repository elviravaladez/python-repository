# Sets are UNORDERED collections of UNIQUE elements (no duplicates)

my_set = set()
print(my_set)
# set()

my_set.add(1)
print(my_set)
# {1}

my_set.add(2)
print(my_set)
# {1, 2}

# If you try to add a value that is already in the set, it will not repeat it
my_set.add(2)
print(my_set)
# {1, 2}

# Sets are useful to cast a list to a set, that we'll only get the unique values for
my_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
print(set(my_list))
# {1, 2, 3}

# Sets don't have an order
