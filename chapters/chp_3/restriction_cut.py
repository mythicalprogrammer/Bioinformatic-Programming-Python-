def restriction_cut(base_seq, recognition_seq, off = 0):
	"""Return a pair of sequences derived from base_seq
	of recognition_seq; offset, which may be negative, is
	the number of bases relative to the beginning of the
	site where the sequence is cut"""
	site = recognition_set(base_seq, recognition_seq)
	return base_seq[:site+offset], base_seq[site+offset:]
