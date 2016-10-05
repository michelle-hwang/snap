#!/usr/local/python/2.7.3/bin/python

from __future__ import print_function
from Bio import SeqIO
import argparse

# -----------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='''
	AUTHOR: Michelle Hwang''')

parser.add_argument('file1', help='File to append to.')
parser.add_argument('file2', help='''File to append.''')

args = parser.parse_args()

file1 = open(args.file1, 'r')
matrix = list()
for line in file1:
	matrix.append(line.rstrip())
file1.close()

new_seqs = dict()
seqiter = SeqIO.parse(open(args.file2), 'fasta')
for seq in seqiter:
	count = seq.id.split("-")[1]
	new_seqs[seq.seq] = count
seqiter.close()


# -----------------------------------------------------------------------------

def main():

	print(matrix[0])

	genes_in_matrix = list()

	for cols in matrix[1:]:
		col = cols.split('\t')
		gene = col[0]
		genes_in_matrix.append(gene)

		for c in col:
			print(c, end='\t')

		if gene in new_seqs:
			print(col[1])
		else:
			print('0')

	for seq, value in new_seqs.iteritems():
		if seq not in genes_in_matrix:
			print(seq, end='\t')
			for n in xrange(1,len(matrix[1].split('\t'))):
				print('0', end='\t')
			print(value)

main()


