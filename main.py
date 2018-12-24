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
		return suffix_array

	def inverse_transform(self):
		string = self.string


def main():
	bwt = BWT('banana')
	print(bwt.transform())

if __name__ == '__main__':
	main()