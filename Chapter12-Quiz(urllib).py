from cgitb import handler
from multiprocessing.connection import answer_challenge


Question 1:

Which of the following Python data structures is most similar to the value returned in this line of Python:

x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

list
socket
dictionary
file handle
regular expression

Ans: file handle

Qusetion 2:

In this Python code, which line actually reads the data?

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

mysock.recv()
socket.socket()
mysock.close()
mysock.connect()
mysock.send()

Ans: mysock.recv()

Question 3:

Which of the following regular expressions would extract the URL from this line of HTML:

<p>Please click <a href="http://www.dr-chuck.com">here</a></p>

href="(.+)"
href=".+"
http://.*
<.*>

Ans: href="(.+)"

Question 4:

In this Python code, which line is most like the open() call to read a file:

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

mysock.connect()
import socket
mysock.recv()
mysock.send()
socket.socket()

Ans: mysock.connect()

Question 5:

Which HTTP header tells the browser the kind of document that is being returned?

Metadata:
Document-Type:
Content-Type:
HTML-Document:
ETag:

Ans: Content-Type:

Question 6:

What should you check before scraping a web site?

That the web site returns HTML for all pages
That the web site only has links within the same site
That the web site allows scraping
That the web site supports the HTTP GET command

Ans: That the web site allows scraping

Question 7:

What is the purpose of the BeautifulSoup Python library?

It repairs and parses HTML to make it easier for a program to understand
It allows a web site to choose an attractive skin
It builds word clouds from web pages
It animates web operations to make them more attractive

Ans: It repairs and parses HTML to make it easier for a program to understand

Question 8:

What ends up in the "x" variable in the following code:

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')

A list of all the anchor tags (<a..) in the HTML from the URL
True if there were any anchor tags in the HTML from the URL
All of the externally linked CSS files in the HTML from the URL
All of the paragraphs of the HTML from the URL

Ans: A list of all the anchor tags (<a..) in the HTML from the URL

Question 9:

What is the most common Unicode encoding when moving data between systems?

UTF-64
UTF-8
UTF-32
UTF-16
UTF-128

Ans: UTF-8

Quesiton 10:

What is the ASCII character that is associated with the decimal value 42?

^
!
*
/
+

Ans: *

Question 11:

What word does the following sequence of numbers represent in ASCII:

108, 105, 110, 101

line
func
tree
ping
lose

Ans: line

Question 12:

How are strings stored internally in Python 3?

UTF-8
ASCII
EBCDIC
Byte Code
Unicode

Ans: Unicode

Question 13:

When reading data across the network (i.e. from a URL) in Python 3, what method must be used to convert it to the internal format used by strings?

find()
trim()
decode()
encode()
upper()

Ans: decode()