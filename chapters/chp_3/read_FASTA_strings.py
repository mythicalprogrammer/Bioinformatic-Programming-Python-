def read_FASTA_strings(filename):
	with open(filename) as file:
		return file.read().split('>')[1:]
