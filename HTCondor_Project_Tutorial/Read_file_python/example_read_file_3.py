# http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/
## Open the file with read only permit
f = open('history.txt', "r")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.readlines()

# Print each line in the list.
for line in lines:
    print line

## close the file after reading the lines.
f.close()
