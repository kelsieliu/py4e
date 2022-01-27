from email.errors import FirstHeaderLineIsContinuationDefect


Question 1:

What is wrong with this Python loop:

n = 5
while n > 0 :
    print(n)
print('All done')

This loop will run forever
The print('All done') statement should be indented four spaces
There should be no colon on the while statement
while is not a Python reserved word

Ans: This loop will run forever

Question 2:

What does the break statement do?

Jumps to the "top" of the loop and starts the next iteration
Exits the currently executing loop
Exits the program
Resets the iteration variable to its initial value

Ans: Exits the currently executing loop

Question 3:

What does the continue statement do?

Exits the program
Exits the currently executing loop
Jumps to the "top" of the loop and starts the next iteration
Resets the iteration variable to its initial value

Ans: Jumps to the "top" of the loop and starts the next iteration

Question 4:

What does the following Python program print out?

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

15
5
0
10

Ans: 5

Question 5:

What is the iteration variable in the following Python code:

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')

friend
Glenn
Sally
Friends

Ans: friend

Question 6:

What is a good description of the following bit of Python code?

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

Sum all the elements of a list
Find the smallest item in a list
Compute the average of the elements in a list
Count all of the elements in a list

Ans: Sum all the elements of a list

Question 7:

What will the following code print out?

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

Hint: This is a trick question and most would say this code has a bug - so read carefully

-1
74
42
3

Ans: -1

Question 8:

What is a good statement to describe the is operator as used in the following if statement:

if smallest is None :
     smallest = value

matches both type and value
Is true if the smallest variable has a value of -1
The if statement is a syntax error
Looks up 'None' in the smallest variable if it is a string

Ans: matches both type and value

Question 9:

Which reserved word indicates the start of an "indefinite" loop in Python?

while
break
indef
def
for

Ans: while

Question 10:

How many times will the body of the following loop be executed?

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

This is an infinite loop
0
1
5

Ans: 0