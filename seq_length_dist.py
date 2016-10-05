
from Bio import SeqIO
import sys

args = str(sys.argv)
for seq_record in SeqIO.parse(str(sys.argv[1]), 'fasta'):
	output_line = '%s\t%i' % \
	(seq_record.id, len(seq_record))
	print(output_line)
