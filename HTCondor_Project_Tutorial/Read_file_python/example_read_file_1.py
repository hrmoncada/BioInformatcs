# Open the file for reading.
with open('history.txt', 'r') as infile:
    data = infile.read()  # Read the contents of the file into memory.

# Return a list of the lines, breaking at line boundaries.
my_list = data.splitlines()
size_list = len(my_list)
print "file size = %d"% size_list

# Print statements for testing purposes:
print my_list  # Print the list.
print my_list[0]  # Print the list line.

# Print each element-line in the list.
for line in my_list:
    print line

# Print the fourth element-line in this list. element-lines: 0,1,2,3
print my_list[3] # element-line 4

# Split each element-line by the parameter (' ', space)
count = 0
vec = [] 
for line in my_list:
    #array_column = line.split(' ')  # Partition line by one space.
    array_column = line.split( )  # Partition line by multiple spaces.
    array_column_2 = line.partition(' ')
    vec.append(float(line.split(' ')[3])) # assign string to a vector array   
    print count, array_column[3] # Print third column elements.
    count += 1

print "count = %d"% count
print "vector\n"
print vec
#print "Sum = %d"% sum(vec)

"""countw = 0
for line in my_list:
      words = line.split()
      for word in words:
          print word
      countw += 1
      if countw == 3:
        break"""

