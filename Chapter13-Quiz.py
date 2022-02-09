from calendar import HTMLCalendar, c
from collections import namedtuple
from platform import python_version_tuple
from re import A
from socket import TCP_CORK
from unicodedata import name


Quiz - eXtensible Markup Language

Question 1:

What is the name of the Python 2.x library to parse XML data?

xml.json
xml-misc
xml2
xml.etree.ElementTree    

Ans: xml.etree.ElementTree    

Question 2:

Which of the following are not commonly used serialization formats?

HTTP
Dictionaries
TCP
JOSN
HTML

Ans: HTTP, DICTIONARIES, TCP_CORK

Question 3:

In this XML, which are the "complex elements"?

<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>

phone
Noah
name
person
people

Ans: name, phone

Question 4:

In the following XML, which are attributes?

<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>

name
person
type
email
hide

Ans: type, hide

Question 5:

In the following XML, which node is the parent node of node e

<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>

b
a
e
c

Ans: c

Question 6:

Looking at the following XML, what text value would we find at path "/a/c/e"

<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>

Y
Z
b
e
a

Ans: Z

Question 7:

What is the purpose of XML Schema?

To establish a contract as to what is valid XML
To transfer XML data reliably during network outages
A Python program to tranform XML files
To compute SHA1 checksums on data to make sure it is not modified in transit

Ans: To establish a contract as to what is valid XML

Question 8:

If you were building an XML Schema and wanted to limit the values allowed in an xs:string field to only those in a particular list, what XML tag would you use in your XML Schema definition?

xs:element
xs:complexType
xs:sequence
maxOccurs
xs:enumeration

Ans: maxOccurs

Question 9:

What does the "Z" mean in this representation of a time:

2002-05-30T09:30:10Z

This time is in the UTC timezone
The hours value is in the range 0-12
The local timezone for this time is New Zealand
This time is Daylight Savings Time

Ans: This time is in the UTC timezone

Question 10:

Which of the following dates is in ISO8601 format?

05/30/2002
May 30, 2002
2002-May-30
2002-05-30T09:30:10Z

Ans:2002-05-30T09:30:10Z