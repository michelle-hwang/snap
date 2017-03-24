

import argparse
import itertools
import operator


parser = argparse.ArgumentParser(description='''
	Parse BLAST outfmt=6 files. 
	AUTHOR: Michelle Hwang''')
parser.add_argument('blast', help="BLAST OUTFMT=6")
parser.add_argument('--n', type=int, default=1, help='Top n results to keep')
parser.add_argument('--e', default=1E-3, type=float, help='''Optional e-value cut-off for
	BLAST results. Default is 1E-3.''')
parser.add_argument('--p', type=float, default=0, help='''Optional percent identity
	cut-off for BLAST results. Default is no filter.''')
parser.add_argument('--g', action='store_true', help='Only consider Trinity genes')
parser.add_argument('--clean', action='store_true', help='Only print query and hit IDs')
parser.add_argument('--swissprot', action='store_true', help='Shorten hit ID to just swissprot ID')
args = parser.parse_args()


def main():

	with open(args.blast) as f:
		lines = f.read().splitlines()

	sequences = []
	sequence_current = None

	for line in lines:

		field = line.split()

		if args.g is True:
			field[0] = field[0].split('_i')[0]
		sequence = field[0]

		if float(field[10]) > args.e or float(field[2]) < args.p:
			continue

		if args.swissprot is True:
			field[1] = field[1].split('|')[2]

		if sequence_current == sequence:
			sequences.append(field)
		else:
			if sequence_current is not None:
				sequences_sorted = sorted(sequences, key=operator.itemgetter(10), reverse=True)
				sequences_sorted = list(x for x,_ in itertools.groupby(sequences_sorted))
				for seq in sequences_sorted[:args.n]:
					if args.clean is True:
						print('\t'.join([str(s) for s in seq[:2]]))
					else:
						print('\t'.join([str(s) for s in seq]))

			sequence_current = sequence
			sequences = []
			sequences.append(field)


main()






