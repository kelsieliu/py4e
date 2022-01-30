Question 1:

Given the architecture and terminology we introduced in Chapter 1, where are files stored?

Motherboard
Central Processor
Main Memory
Secondary memory

Ans: Secondary memory

Question 2:

What is stored in a "file handle" that is returned from a successful open() call?

All the data from the file is read into memory and stored in the handle
The handle contains the first 10 lines of a file
The handle is a connection to the file's data
The handle has a list of all of the files in a particular folder on the hard drive

Ans: The handle is a connection to the file's data

Question 3:

What do we use the second parameter of the open() call to indicate?

How large we expect the file to be
What disk drive the file is stored on
Whether we want to read data from the file or write data to the file
The list of folders to be searched to find the file we want to open

Ans: Whether we want to read data from the file or write data to the file

Question 4:

What Python function would you use if you wanted to prompt the user for a file name to open?

input()
read()
cin
file_input()

Ans: input()

Question 5:

What is the purpose of the newline character in text files?

It enables random movement throughout the file 
It allows us to open more than one files and read them in a synchronized manner
It adds a new network connection to retrieve files from the network
It indicates the end of one line of text and the beginning of another line of text

Ans: It indicates the end of one line of text and the beginning of another line of text

Question 6:

If we open a file as follows:
xfile = open('mbox.txt')

What statement would we use to read the file one line at a time?

while ( getline (xfile,line) ) {
while (<xfile>) {
for line in xfile:
READ (xfile,*,END=10) line

Ans: for line in xfile:

Question 7:

What is the purpose of the following Python code?

fhand = open('mbox.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)

Convert the lines in mbox.txt to upper case
Reverse the order of the lines in mbox.txt
Count the lines in the file 'mbox.txt'
Remove the leading and trailing spaces from each line in mbox.txt

Ans: Count the lines in the file 'mbox.txt'

Question 8:

If you write a Python program to read a text file and you see extra blank lines in the output that are not present in the file input as shown below, what Python string function will likely solve the problem?

From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

...

rstrip()
ljust()
startswith()
find()

Ans: rstrip()

Queston 9:

The following code sequence fails with a traceback when the user enters a file that does not exist.  How would you avoid the traceback and make it so you could print out your own error message when a bad file name was entered?

fname = input('Enter the file name: ')
fhand = open(fname)

begin / rescue / end
on error resume next
try / except
setjmp / longjmp

Ans: try / except

Question 10:

What does the following Python code do?

fhand = open('mbox-short.txt')
inp = fhand.read()

Checks to see if the file exists and can be written
Prompts the user for a file name
Reads the entire file into the variable inp as a string
Turns the text in the file into a graphic image like a PNG or JPG

Ans: Reads the entire file into the variable inp as a string