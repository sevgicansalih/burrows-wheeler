class BWT():
	"""docstring for BWT"""
	def __init__(self, string):
		if '$' in string:
			self.string = string
		else:
			self.string = string+'$'

	def transform(self):
		string = self.string
		length = len(string)
		suffix_array = []
		for i in range(length):
			string = string[-1] + string[0:length-1]
			suffix_array.append(string)
		sorted_suffix = sorted(suffix_array)
		result = ''
		for suffix in sorted_suffix:
			result += suffix[-1]
		return result

	def inverse_transform(self):
		string = self.string


def main():
	bwt = BWT('GCGTGCCTGGTCA$')
	t = bwt.transform()
	print(t)
	res = 'ACTGGCT$TGCGGC'
	print (res == t)

if __name__ == '__main__':
	main()