def validate_base_sequence(base_sequence, RNAflag = False):
	"""Return True if the string base_sequence contains only upper- or
	T (or U, if RNAflag), C, A, and G characters, otherwise False"""
	DNAbases = set('TCAGtcag')
	RNAbases = set('UCAGucag')
	return set(base_sequence).issubset(RNAbases if RNAflag else DNAbases)
