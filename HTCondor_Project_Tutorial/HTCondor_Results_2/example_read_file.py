#!/usr/bin/python

# Open the file for reading.
#with open('history_7.txt', 'r') as infile:
with open('data_history_6_16_12.txt', 'r') as infile:
    data = infile.read()  # Read the contents of the file into memory.

# Return a list of the lines, The data file is breaking into line (rows).
my_list = data.splitlines()

# Get and print the number of lines (rows)
size_list = len(my_list) 
print "file size = %d  rows"% size_list

# Print statements for testing purposes:
#print my_list  # Print the list.
#print my_list[0]  # Print the list line.
#print my_list[1]  # Print the list line.
# Split each line by the parameter (' ', space)

#Start Counter
count = 0

# Set vector arrays
Count = []
min_Start = []
min_End = []
sec_Start = []
sec_End = []
ID = []
Run_Time = []
Run_Time_min = []
Run_Time_sec = []

for line in my_list:
  if count > 0: # Don't read the first row
    #array_column = line.split(' ')  # Partition row line by one space.
    array_column = line.split( )  # Partition row line by multiple spaces.
    #array_column_2 = line.partition(' ')

    array_column_Start = array_column[3].split(':')
    array_column_End   = array_column[7].split(':')

    array_column_Run_Time = array_column[4].split('+')
    Run_Time =  array_column_Run_Time[1].split(':')

    size = len(array_column)
    size_Start = len(array_column_Start)
    size_End = len(array_column_End)
 #   end_time.append(float(array_column[7].split(':')[0]) + float(array_column[7].split(':')[-1])) 
 #   print count, size, size_Start,size_End, array_column[0], array_column_Start[0], array_column_Start[-1],  array_column_End[0], array_column_End[-1] # Print third column elements.
    ID.append(float(line.split(' ')[3])) # assign string (on column 3) to a vector array   
    min_Start.append(float(array_column_Start[0]))
    sec_Start.append(float(array_column_Start[-1]))
    min_End.append(float(array_column_End[0]))
    sec_End.append(float(array_column_End[-1]))
    Run_Time_min.append(float(Run_Time[1]))
    Run_Time_sec.append(float(Run_Time[2]))

    #print count, array_column[0], array_column_Start[0], array_column_Start[-1],  array_column_End[0], array_column_End[-1], array_column_Run_Time[1],Run_Time[0],Run_Time[1],Run_Time[2]# Print third column elements.
    #if count == 10:
    #    break
  count += 1

#print "End Time = %d"% max(array_column[7])

print "count = %d"% count

#print ID
#for value in ID:
#    print(value)
#    print "%4.3f"% value

#print "             Submitted    Completed"
#print "Count  ID    min   sec    min   sec     End    Start"
#for i in range(0, count): # text count = 10 
#for i in range(0, count-1): # full file
#    print "   %d  %4.3f   %d    %d     %d    %d    %d     %d" %  (i, ID[i], min_Start[i], sec_Start[i], min_End[i], sec_End[i],min_End[i]*60.0 + sec_End[i], min_Start[i]*60.0 + sec_Start[i])


print "Count   ID    End    Start    TIME  Run Time"
for i in range(0, count-1): # full file
  #print "   %d  %4.3f   %d    %d     %d" %  (i, ID[i], min_End[i]*60.0 + sec_End[i], min_Start[i]*60.0 + sec_Start[i], min_End[i]*60.0 + sec_End[i]- min_Start[i]*60.0 + sec_Start[i])
  print "   %d  %4.3f   %d    %d     %d    %d" %  (i, ID[i], min_End[i]*60.0 + sec_End[i], min_Start[i]*60.0 + sec_Start[i], min_End[i]*60.0 + sec_End[i]- min_Start[i]*60.0 + sec_Start[i], Run_Time_min[i]*60 + Run_Time_sec[i])
  if i == 10:
     raw_input("Press Enter to continue...")


#print len(min_Start)
#print "\n" #"Sum = %d"% sum(vec)"""
#print len(sec_Start)

#for i in 10:
#  Start[i] = min_Start[i]*60.0 + sec_Start[i] 

