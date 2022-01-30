Question 1:

How are Python dictionaries different from site import check_enableusersite
from Python lists?

Python lists store multiple values and dictionaries store a single value
Python dictionaries are a collection and lists are not a collection
Python lists are indexed using integers and dictionaries can use strings as indexes
Python lists can store strings and dictionaries can only store words

Ans: Python lists are indexed using integers and dictionaries can use strings as indexes

Question 2:

What is a term commonly used to describe the Python dictionary feature in other programming languages?

Closures
Associative arrays
Lambdas
Sequences

Ans: Associative arrays

Question 3:

What would the following Python code print out?

stuff = dict()
print(stuff['candy'])

-1
candy
0
The program would fail with a traceback

Ans: The program would fail with a traceback

Question 4:

What would the following Python code print out?

stuff = dict()
print(stuff.get('candy',-1))

0
-1
The program would fail with a traceback
'candy'

Ans: -1

Question 5:

(T/F) When you add items to a dictionary they remain in the order in which you added them.

False
True

Ans: False

Question 6:

What is a common use of Python dictionaries in a program?

Splitting a line of input into words using a space as a delimiter
Computing an average of a set of numbers
Building a histogram counting the occurrences of various strings in a file
Sorting a list of names into alphabetical order

Ans: Building a histogram counting the occurrences of various strings in a file

Question 7:

Which of the following lines of Python is equivalent to the following sequence of statements assuming that counts is a dictionary?

if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1

counts[key] = (counts[key] * 1) + 1
counts[key] = counts.get(key,-1) + 1
counts[key] = key + 1
counts[key] = counts.get(key,0) + 1
counts[key] =  (key in counts) + 1

Ans: counts[key] = counts.get(key,0) + 1

Question 8:

In the following Python, what does the for loop iterate through?

x = dict()
...
for y in x :
     ...

It loops through all of the dictionaries in the program
It loops through the keys in the dictionary
It loops through the integers in the range from zero through the length of the dictionary
It loops through the values in the dictionary

Ans: It loops through the keys in the dictionary

Question 9:

Which method in a dictionary object gives you a list of the values in the dictionary?

each()
values()
keys()
items()
all()

Ans: values

Question 10:

What is the purpose of the second parameter of the get() method for Python dictionaries?

To provide a default value if the key is not found
An alternate key to use if the first key cannot be found
The value to retrieve
The key to retrieve

Ans: To provide a default value if the key is not found