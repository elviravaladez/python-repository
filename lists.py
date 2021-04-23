my_list = [1,2,3]
my_list_two = ['String',100,23.2]
len(my_list) # 3

my_list = ['one','two','three']
print(my_list[0])
# one

another_list = ['four', 'five']

print(my_list + another_list)
# ['one', 'two', 'three', 'four', 'five']

new_list = my_list + another_list
# ['one', 'two', 'three', 'four', 'five']

new_list[0] = 'ONE ALL CAPS'

print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

# Add an element to the list

new_list.append('six')
# This effects the list in place

print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']

new_list.append('seven')

print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'seven]

new_list.pop()
# 'seven'

print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']

popped_item = new_list.pop()
# 'six'

print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

# REMOVE AT A SPECIFIC INDEX
new_list.pop(0)
# 'ONE ALL CAPS'

print(new_list)
# ['two', 'three', 'four', 'five']

# REVERSE INDEXING ALSO WORKS WITH LISTS

# POPULAR METHODS
# pop()
# append()
# sort()  -> in place method (does not return anything)
# reverse()  -> in place method (does not return anything)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]


# SORT METHOD
new_list.sort()
# the sort method is a special in place method (IT DOESN'T RETURN ANYTHING) but it does sort the list

# DO NOT TRY TO SAVE new_list.sort() to a variable b/c it will return NoneType
# EX. (DON'T DO THIS):
my_sorted_list = new_list.sort()
# IntelliJ message: "Function 'sort' doesn't return anything"
print(type(my_sorted_list))
# <class 'NoneType'>

# There is a special object called NONE that is a return value for functions that don't return anything

print(new_list)
# ['a', 'b', 'c', 'e', 'x']


# DO THIS INSTEAD
new_list.sort()
my_sorted_list = new_list

print(my_sorted_list)
# ['a', 'b', 'c', 'e', 'x']

print(num_list)
# [4, 1, 8, 3]

num_list.sort()

print(num_list)
# [1, 3, 4, 8]


# REVERSE METHOD
# the reverse method is a special in place method (IT DOESN'T RETURN ANYTHING) but it does reverse the list

num_list.reverse()

# DO NOT TRY TO SAVE num_list.reverse() to a variable b/c it will return NoneType
# EX. (DON'T DO THIS):
my_reversed_num_list = num_list.reverse()

print(type(my_reversed_num_list))
# <class 'NoneType'>

# DO THIS INSTEAD
num_list.reverse()

print(num_list)
# [8, 4, 3, 1]

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_number_list = number_list[:3] + number_list[7:]
# including numbers [1, 2, 3] + [8, 9]

# # Display sliced list
print(new_number_list)
# [1, 2, 3, 8, 9]

mixed_string = [1, 'two', 3.14159]

print(mixed_string)
