# Load modules
from Bio import SeqIO  # module needed for sequence input  
import sys             # module needed for command line argument to get fastq name  
import re              # module for Regular expression operations, this module provides regular expression matching operations similar to those found in Perl.
import subprocess

# Compiler and path tool
ja = " java -jar"
tool = " /usr/local/TRIMHOME/trimmomatic.jar"
s = " "
# Execute Single end or Paired end
mode = raw_input("Please enter enter mode (Single [1]  or Paired [2]): ")
print 'Mode = ', mode

if mode == 'Single' or mode == '1':  
   print "Sigle End mode : Supply fastq file\n"
   # Load data 
   file_input = "/home/henry/Desktop/RNA_Seq_Differential_Expressions/FASTQ_Files/single_end/ERR458493.fastq"
   fastqfile1 = open(file_input, 'r') 
   # Output single end
   file_output = "/home/henry/Desktop/RNA_Seq_Differential_Expressions/FASTQ_Files/single_end/output_single_ERR458493.fastq"
   # FASTQ file where you want to trim all the reads
   count = 0
   for rec in SeqIO.parse(fastqfile1, "fastq"):
      count += 1
   print("farsq %i reads\n" % count)   # count reads

   print "Start Trimmonatics :"    #java -jar trimmomatic SE -threads 4 -phred33 file_input file_output ILLUMINACLIP:adapters:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
   print "--------------------" 
   attribute              = " SE -threads 4 -phred33"
   illuminaclip_adapters  = "ILLUMINACLIP:/usr/local/TRIMHOME/adapters/TruSeq3-SE.fa:2:30:10"
   illuminaclip_Attribute = "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"
   cmd  = s + ja + s + tool + s + attribute + s + file_input + s + file_output + s + illuminaclip_adapters + s + illuminaclip_Attribute
   call = ["/bin/bash", "-c", cmd]
   ret  = subprocess.call(call, stdout=None, stderr=None)
   if ret > 0:
      print "Warning - result was %d" % ret

elif mode == 'Paired' or mode == '2': 
   print "Paired End mode: Supply a forward and reverse fastq files\n"
# Load data forward
   filename_forward = "/home/henry/Desktop/RNA_Seq_Differential_Expressions/FASTQ_Files/paired_end/ERR950159_1.fastq"
   fastq_forward = open(filename_forward, 'r')  # Here you write your fastq filename
   # FASTQ file where you want to trim all the reads
   #count = 0
   #for rec in SeqIO.parse(fastq_forward, "fastq"):
   #   count += 1
   #print("fastq forward %i reads" % count)   # count reads

   # Load data reverse
   filename_reverse = "/home/henry/Desktop/RNA_Seq_Differential_Expressions/FASTQ_Files/paired_end/ERR950159_2.fastq"
   fastq_reverse = open(filename_reverse, 'r') 
   # FASTQ file where you want to trim all the reads
   #count = 0
   #for rec in SeqIO.parse(fastq_reverse, "fastq"):
   #   count += 1
   #print("fastq reverse %i reads" % count)   # count reads

   # Outputs paired end
   output_forward_paired = "/home/henry/Desktop/RNA_Seq_Differential_Expressions/FASTQ_Files/paired_end/output_forward_paired_ERR950159_1.fastq" 
   output_forward_unpaired = "/home/henry/Desktop/RNA_Seq_Differential_Expressions/FASTQ_Files/paired_end/output_forward_unpaired_ERR950159_1.fastq" 
   output_reverse_paired = "/home/henry/Desktop/RNA_Seq_Differential_Expressions/FASTQ_Files/paired_end/output_reverse_paired_ERR950159_2.fastq"  
   output_reverse_unpaired = "/home/henry/Desktop/RNA_Seq_Differential_Expressions/FASTQ_Files/paired_end/output_reverse_unpaired_ERR950159_2.fastq" 

   print "Start Trimmonatics :"    
   print "--------------------" 
   attribute              = "PE -threads 12 -phred33 "
   illuminaclip_adapters  = "ILLUMINACLIP:/usr/local/TRIMHOME/adapters/TruSeq3-PE.fa:2:30:10"
   illuminaclip_Attribute = "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"
   cmd1 = s + ja + s + tool + s + attribute + s + filename_forward + s + filename_reverse + s + output_forward_paired + s + output_forward_unpaired
   cmd2 = s + output_reverse_paired + s + output_reverse_unpaired + s + illuminaclip_adapters + s + illuminaclip_Attribute
   cmd  =  cmd1 + cmd2
   call = ["/bin/bash", "-c", cmd]
   ret  = subprocess.call(call, stdout=None, stderr=None)
   if ret > 0:
      print "Warning - result was %d" % ret


