# Python

This is a repository to document my progress while learning Python.

## Table of Contents

- [Overview](#overview)
    - [The Objective](#the-objective)
- [My Process](#my-process)
    - [Built With](#built-with)
    - [What I Learned](#what-i-learned)
    - [Continued Development](#continued-development)
- [Author](#author)

## Overview

### The Objective

Understand the fundamentals of Python.

## My Process

### Built With

- Python
- IntelliJ IDEA

### What I Learned

#### Data Types

|Name|Type|Description|
|---|---|---|
|Integers 🔢|int|Whole numbers, such as: 1, 120, 300|
|Floating Point 🎈|float|Numbers with a decimal point 1.2, 120.5, 500.0|
|Strings 🧵|str|Ordered sequence of characters: "hi" 'hola' '4029'|
|Lists 📝|list|Ordered sequence of objects: [50,"hola",512.0]|
|Dictionaries 📕|dict|Unordered Key:Value pairs: {"mykey":"value","name":"Elvira"}|
|Tuples 🛁|tup|Ordered immutable sequence of objects:(23,"hola",313.4)|
|Sets 👡👠|set|Unordered collection of unique objects: {"a","b"}|
|Booleans ✅ 🚫️|bool|Logical value indicating True or False|


#### Variables

* It is recommended that variable names be lowercase
* Cannot start with a number
* No spaces. An underscore is recommended instead: _
* Does not allow certain symbols
* Python is dynamically typed
  * You can reassign variables to different data types
  * Python is very flexible in assigning data types

#### Strings

Today I learned that Python has reverse indexing. One example of when this can be useful is when you want to grab the last letter of a string. In this case, you would use -1.

#### I/O with Basic Files

 You can create basic files, such as txt files, using jupyter notebooks.

Example of how to write a file using a `ipynb` juptyer notebook:
```jupyterpython
%%writefile filename.txt
This is the plain text that will be written on the file
```

`filename.txt` example
```txt
This is the plain text that will be written on the file
```

When creating a basic txt file using jupyter notebooks, there are some basic functions/methods we can use.

#### open() function

The code snippet below is an example of the `open()` function

```jupyterpython
filename = open('filename.txt')
```

The example above will not give an error because, the file was written within the jupyter notebook.

However, the following code snippet will output an error, because the `wrong_filename.txt` file I am trying to open does not exist, OR an incorrect file path was provided:

```jupyterpython
filename = open('wrong_filename.txt')

---------------------------------------------------------------------------

FileNotFoundError                         Traceback (most recent call last)

<ipython-input-5-8d94c7c80b4a> in <module>
----> 1 myfile = open('wrong_filename.txt')

FileNotFoundError: [Errno 2] No such file or directory: 'wrong_filename.txt'
```

#### read() method

The read method returns a string of everything that's within the txt file you are reading.

```jupyterpython
filename = open('filename.txt')

filename.read()
# output:'This is the plain text that will be written on the file'
```

#### seek() method

If you are trying to re-read a txt file after running the read() method an initial time, you must reset the 'cursor' to 0 to read the file from the beginning.

```jupyterpython
filename.seek(0)
# output: 0

contents = filename.read()
contents
# output:'This is the plain text that will be written on the file'
```

If you do not reset the 'cursor,' the outcome will be:
```jupyterpython
filename.read()
# output: ''
```

### Continued Development

This section will outline areas that I want to continue focusing on in future projects.

---

## Author

[Elvira Valadez](https://github.com/elviravaladez)

---

### [Back To The Top](#python)