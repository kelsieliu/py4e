Python for Everybody - A Review

Question 1:

What is the most common Unicode encoding when moving data between systems?

UTF-8
UTF-64
UTF-32
UTF-128
UTF-16

Ans: UTF-8

Question 2:

What is the decimal (Base-10) numeric value for the upper case letter "G" in the ASCII character set?

2048
17
71
1771
7

Ans: 71

Question 3:

What word does the following sequence of numbers represent in ASCII:

108, 105, 115, 116

http
open
list
fuss
lost

Ans: list

Question 4:

How are strings stored internally in Python 3?

UTF-16
Latin
Unicode
EBCDIC
ASCII

Ans: Unicode

Question 5:

When reading data across the network (i.e. from a URL) in Python 3, what method must be used to convert it to the internal format used by strings? 

decode()
msub()
encode()
convert()
more()

Ans: decode()

Quesiton 6:

Which of the following lines will never print out regardless of the value of "x"?

if x < 2 :
    print("Below 2")
elif x < 0 :
    print("Negative")
else :
    print("Something else")

Something else
All the lines will print out
Negative
Below 2

Ans: Negative

Question 7:

Which of the following lines will never print out regardless of the value for x?

if x < 2 :
    print("Below 2")
elif x < 20 :
    print("Below 20")
elif x < 10 :
    print("Below 10")
else :
    print("Something else")

Below 10
Below 20
Something else
Below 2

Ans: Below 10

Question 8:

What would the following Python code sequence print out?

zap = "hello there bob"
print(zap[4])

You would get an out-of-range error and the program would fail

zap
l
o
hello

Ans: o

Question 9:

Which of the following lines of Python code contains a syntax error?

x = 12
if x < 5:
print("smaller")
else:
    print("bigger")
print("all done")

Ans: 3

Question 10:

What will the following Python program print out?

def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()

ABC Zap jane
Zap Zap Zap
Zap ABC Zap
Zap ABC jane fred jane
ABC Zap ABC

Ans: ABC Zap ABC

Question 11:

Where in the computer is a variable such as "X" stored?

x = 123

Main Memory
Output Devices
Central processing unit
Input Devices
Secondary Memory

Ans: Main Memory

Quesiton 12:

What is the primary use of the Python dictionary?

To make sure that the definitions of the Python reserved words are available in different languages (French, Spanish, etc)
To store key / value pairs
To look up all of the methods which are available on a Python object
To insure that all Python reserved words are properly spelled

Ans: To store key / value pairs

Question 13:

What does the following Python code print out? 

stuff = ['joseph', 'sally', 'walter', 'tim']
print(stuff[2])

walter
sally
joseph
tim

Ans: walter

Question 14:

What will the following Python program print out?  (This is a bit tricky so look carefully).

def hello():
    print("Hello")
    print("There")

x = 10
x = x + 1

11
Nothing will print
x = 11
Hello
There
11

Ans: Nothing will print

Question 15:

What will the following Python program print out?

x = -1
for value in [3, 41, 12, 9, 74, 15] :
    if value > x :
        x = value
print(x)

74
9
-1
15
3

Ans: 74

Question 16:

What will the following Python program print out?

total = 0
for abc in range(5):
    total = total + abc
print(total)

16
10
6
5
4

Ans: 10

Question 17:

The following Python code causes a traceback:

a = "123"
b = 456
c = a + b
print(c)

Which line fails with a traceback?

3
1
2
4

Ans: 3

Question 18:

In the following example, an error occurs in "line3" that normally causes a traceback if it were not in a try/except.

line1
try:
     line2
     line3
     line4
except:
     line5
line6

What is the sequence of lines executed in this program?

line1, line5, line6
line1, line2, line3, line5, line6
line1, line4, line5, line6
line1, line2, line3,  line6
line1, line2, line3, line4, line5, line6

Ans: line1, line2, line3, line5, line6

Question 19:

What would the following Python code print out?

abc = "With three words"
stuff = abc.split()
print(stuff)

['With the', 'ee words']
['w', 'i', 't', 'h']
['With', 'three', 'words']
['With three words']
['With', 'three words']

Ans: ['With', 'three', 'words']

Question 20:

What would the following Python code print out?

abc = "With three words"
stuff = abc.split()
print(len(stuff))

3
1
14
16
2

Ans: 3

Question 21:

Which of the following is not a good synonym for "class" in Python?

direction
blueprint
pattern
template

Ans: template

Question 22:

What is "self" typically used in a Python method within a class?

To terminate a loop
To set the residual value in an expression where the method is used
The number of parameters to the method
To refer to the instance in which the method is being called

Ans: To refer to the instance in which the method is being called

Question 23:

How is a Python socket different than a Python file handle?

You can read and write using the same socket     
Opening a socket will never fail, while opening a file can fail
The socket does not read all of the data when it is opened

Ans: You can read and write using the same socket  

Question 24:

In the following XML, what is "type"?

<person>
   <name>Chuck</name>
   <phone type="intl">
	  +1 734 303 4456
   </phone>
   <email hide="yes" />
</person>

An attribute
XML syntax error
Value
Tag
Complex element
Simple element

Ans: An attribute

Question 25:

Which programming language serves as the basis for the JSON syntax?

JavaScript
SCALA
Python
Java
PHP

Ans: JavaScript