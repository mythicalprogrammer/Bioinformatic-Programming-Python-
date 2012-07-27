def read_FASTA_entries(filename):
	return [seq.partition('\n') for seq in read_FASTA_strings(filename)]
