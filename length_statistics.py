
import argparse
import sys


## Command line parameters and help
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
	description='''
This script will take in a FASTQ file of small RNA reads and output a tab-delimited
text file containing normalized and adjusted values for each length in order to make
comparisons across libraries.

Default usage:

	python3 length_statistics.py fasta.fq outfile.txt

///AUTHOR: Michelle Hwang
///DATE: 10/8/2015''')
parser.add_argument('fasta', help = 'Name of fasta or fastq file input.')
parser.add_argument('-o', '--outfile', help = 'Name of output file.')
parser.add_argument('-p', '--print_out', type = bool, default = False, help = '''Default is False.
	Set to True to print to standard output''')
parser.add_argument('-q', '--fastq', type = bool, default = False, help = '''Default is False.
	Set to True if file is a FASTQ file.''')


args = parser.parse_args()
fasta = open(args.fasta, 'r')
print_bool = args.print_out
fastq = args.fastq

if(print_bool==False):
	outfile = open(args.outfile, 'w')


## Parse
db = dict()
total = 0
line_num = 1

if(fastq==True):
	for line in fasta:
		if (line_num is 2) or ((line_num-2)%4 == 0):
			total += 1 # Total num reads
			l = len(line.rstrip())
			if l in db:
				db[l] += 1
			else:
				db[l] = 1
		line_num += 1	
elif(fastq==False):
	for line in fasta:
		if '>' not in line:
			total += 1 # Total num reads
			l = len(line.rstrip())
			if l in db:
				db[l] += 1
			else:
				db[l] = 1
		line_num += 1		

	

## Print out stats
if(print_bool==False):
	print("class", "num_reads", "norm_reads", "adj_reads", sep="\t", file=outfile) # Header
else:
	print("class", "num_reads", "norm_reads", "adj_reads", sep="\t") # Header


start = 15
for x in range(0, len(db)):
	read = start + x
	if(print_bool==False):
		print(read, db[read], db[read]/total, (db[read]/total)*1000000, sep='\t', file=outfile)
	else:
		print(read, db[read], db[read]/total, (db[read]/total)*1000000, sep='\t')


if(print_bool==False):
	print("total", total, sep="\t", file=outfile)
else:
	print("total", total, sep="\t")


fasta.close()
if(print_bool==False):
	outfile.close()
