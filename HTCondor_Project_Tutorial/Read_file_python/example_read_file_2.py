## Pass files into the program
## $ python example_read_file_2.py  history.txt 

## reader file
import fileinput

content = []
for line in fileinput.input():
    content.append(line.strip())

# Print statements for testing purposes:
print content  # Print the list.

# Print each line in the list.
for line in content:
    print line

# Print the fourth element in this list.
print content[3]

fileinput.close()
