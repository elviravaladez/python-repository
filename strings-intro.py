# Strings are sequences of characters, using the syntax of either single or double quotes
# Example:
# 'hey'
# "Hey"
# " I don't just like Python. I love it! "

# Strings are ORDERED SEQUENCES
# Uses indexing and slicing to grab sub-sections of the string

# These actions use [] square brackets and a number index to indicate postions of what you wish to grab

#     Character: h  e  l  l  o
#         Index: 0  1  2  3  4
# Reverse Index: 0 -4 -3 -2 -1

print('hello')

print("world")

print('this is also a string')

print(" I'm going on a run ")

print("hello friend one(:")

print("hello friend two(:")

print('hello \nworld')

print(len("hello"))
# 5


# INDEXING WITH STRINGS
my_string = 'Hello World'

print(my_string[0])
# H

print(my_string[8])
# r

# reverse indexing
print(my_string[-1])
# d

print(my_string[-3])
# r

my_string = 'abcdefghijk'

print(my_string[2])
# c

print(my_string[2:])
# cdefghijk


# stop index goes up to 3 but does not include it
print(my_string[:3])
# abc


# Getting subsection that's in the middle of the string
print(my_string[3:6])
# def

print(my_string[1:3])
# bc

# Getting everything from the beginning to the end of the string
# step size of one is the default
print(my_string[::])
# abcdefghijk


# step size of two (skips every other letter)
print(my_string[::2])
# acegik

print(my_string[::3])
# adgj

# [start:stop:step size]


# Can do this as well

# How to reverse a string with Python ;)
print(my_string[::-1])
# kjihgfedcba

string_slice = 'tinker'
print(string_slice[1:4])
# ink


# IMMUTABILITY
# Strings cannot MUTATE

name = "Donny"

# name[4] = 't' <= this does not work!

last_letters = name[1:]
# onny

print('B' + last_letters)
# Bonny

x = 'Hello World '

print(x + "it is beautiful outside")
# Hello World it is beautiful outside

x = x + "it is beautiful outside"

print(x)


# YOU CAN DO MULTIPLICATION CONCATENATION

letter = 'z'
print(letter * 10)
# zzzzzzzzzz

# You will get errors if you try to concatenate a number with a string
print(2 + 3)
# 5

print('2' + '3')
# 23

x = 'Hello World'

print(x.upper())
# HELLO WORLD

print(x.lower())
# hello world

print(x.split())
# Creates a list based on the white space or based on the letters passed
# ['Hello', 'World']

y = "Hi this is a string"
print(y.split())
# ['Hi', 'this', 'is', 'a', 'string']


# SPLITS AT EVERY LETTER "I"
print(y.split('i'))
# ['H', ' th', 's ', 's a str', 'ng']

