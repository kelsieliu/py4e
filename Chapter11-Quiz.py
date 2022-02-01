Question 1:

Which of the following best describes "Regular Expressions"?

The way Python handles and recovers from inspect import getlineno
from errors that would otherwise cause a traceback
A small programming language unto itself
A way to solve Algebra formulas for the unknown value
A way to calculate mathematical values paying attention to operator precedence

Ans: A small programming language unto itself

Question 2:

Which of the following is the way we match the "start of a line" in a regular expression?

^
str.startswith()
\linestart
String.startsWith()
variable[0:1]

Ans: ^

Question 3:

What would the following mean in a regular expression? [a-z0-9]

Match any number of lowercase letters followed by any number of digits
Match a lowercase letter or a digit
Match an entire line as long as it is lowercase letters or digits
Match any text that is surrounded by square braces
Match anything but a lowercase letter or digit

Ans: Match a lowercase letter or a digit

Question 4:

What is the type of the return value of the re.findall() method?

A string
A single character
An integer
A boolean
A list of strings

Ans: A list of strings

Question 5:

What is the "wild card" character in a regular expression (i.e., the character that matches any character)?

^
.
+
$
?
*

Ans: .

Question 6:

What is the difference between the "+" and "*" character in regular expressions?

The "+" matches at least one character and the "*" matches zero or more characters
The "+" matches upper case characters and the "*" matches lowercase characters
The "+" matches the beginning of a line and the "*" matches the end of a line
The "+" matches the actual plus character and the "*" matches any character
The "+" indicates "start of extraction" and the "*" indicates the "end of extraction"

Ans: The "+" matches at least one character and the "*" matches zero or more characters

Question 7:

What does the "[0-9]+" match in a regular expression?

Several digits followed by a plus sign
Zero or more digits
One or more digits
Any number of digits at the beginning of a line
Any mathematical expression

Ans: One or more digits

Question 8:

What does the following Python sequence print out?

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

['From: Using the :']
^F.+:
From:
['From:']
:

Ans: ['From: Using the :']

Question 9:

What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?

^
++
?
**
\g
$

Ans: ?

Question 10:

Given the following line of text:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

What would the regular expression '\S+?@\S+' match?

\@\
From 
stephen.marquard@uct.ac.za
marquard@uct
d@uct.ac.za

Ans: stephen.marquard@uct.ac.za