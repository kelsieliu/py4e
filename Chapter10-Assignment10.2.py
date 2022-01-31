10.2 Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the hour out
from the 'From ' line by finding the time and then splitting the string a second time
using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

Desired Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

Code:
fname = input("Enter file name:")
fhandle = open(fname)

counts = dict()
for line in fhandle:
    if line.startswith("From") and len(line.split())>3:
        words = line.split()
    	time = words[5]
        counts[time[0:2]] = counts.get(time[0:2],0) + 1
    else:
        continue

lst = list()        
for key,value in counts.items():
    lst.append((key,value))

lst.sort()
for key,value in lst:
    print(key,value)

Your Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
