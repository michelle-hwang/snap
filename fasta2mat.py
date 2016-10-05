
from __future__ import print_function
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description='''
	Converts a fastx-toolkit collapsed FASTA file to
	a single column count matrix.

	AUTHOR: Michelle Hwang''')

parser.add_argument('fasta', help='Name of FASTA file.')
args = parser.parse_args()


def main():
	print('\tsample1')

	seqiter = SeqIO.parse(open(args.fasta), 'fasta')
	for seq in seqiter:
		s = seq.id.split('-')
		print(seq.seq, s[1], sep='\t')
	seqiter.close()

main()
