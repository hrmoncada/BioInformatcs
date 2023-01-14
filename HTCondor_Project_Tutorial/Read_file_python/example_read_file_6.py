#!/usr/bin/python
## http://www.tutorialspoint.com/python/file_readline.htm
# Open a file
fo = open("history.txt", "rw+")
print "Name of the file: ", fo.name

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print "Read Line: %s" % (line)

line = fo.readline(5)
print "Read Line: %s" % (line)
print "\n\n"
# Close opend file
fo.close()
