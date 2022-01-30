9.4 Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail. The
program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.

Desired Output
cwen@iupui.edu 5

Code:
fname = input("Enter file name:")
fhandle = open(fname)

counts = dict()

for line in fhandle:
    line.rstrip()
    if line.startswith("From") and len(line.split())>3:
        words = line.split()
        counts[words[1]] = counts.get(words[1],0) + 1
    else:
        continue

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword,bigcount)

Your Output
cwen@iupui.edu 5