#!/usr/bin/python

# Open a file in write mode
fo = open("foo.txt", "rw+")
print "Name of the file: ", fo.name

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

"""seek arguments : The whence argument is optional and defaults to 0, which means absolute file positioning,
                    other values are 1 which means seek relative to the current position and 2 means seek
                    relative to the file's end"""

line = fo.readline()
print "Read Line: %s" % (line)

# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print "Read Line: %s" % (line)

str = "This is 6th line"
# Write a line at the end of the file.
fo.seek(0, 0)
line = fo.write(str)
#print fo.next()

# Now read complete file from beginning.
fo.seek(0,0)
for index in range(6):
   line = fo.next()
   print "\n Line No %d - %s" % (index, line)

# Close opend file
fo.close()

