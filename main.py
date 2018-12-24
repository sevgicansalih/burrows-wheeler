import pandas as pd
import sys

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
		# calculate suffix array
		for i in range(length):
			string = string[-1] + string[0:length-1]
			suffix_array.append(string)
		# sort them
		sorted_suffix = sorted(suffix_array)
		
		#get the last elements of suffix array
		result = ''
		for suffix in sorted_suffix:
			result += suffix[-1]
		return result

	def inverse_transform(self):
		string = self.string
		if '$' not in string:
			return 'No dollar sign detected, terminated.'
		length = len(string)

		# creates empty table
		df = pd.DataFrame()
		df['original'] = list(string)
		# iterates and adds original index everytime, than sorts them
		for i in range(length):
			df[i] = list(string)
			df.set_index(i,inplace=True)
			df.sort_index(inplace = True)
			df.reset_index(inplace = True)

		# deleting excessive column
		df.drop('original',axis = 1,inplace = True)

		# get the row ends with $ sign
		df = df[df[0] =='$']

		# convert to string from dataframe object
		result = ''
		for col in df:
			if col != 'index':
				result += (str((df[col].values[0])))

		return (result)

def main():
	try:	
		command = sys.argv[1]
		#print(command, string)
	except:
		print('You\'ve typed wrond command\n Example command : python3 main.py {bwt - i_bwt}')

	if command == 'bwt':
		string = input('Please type string : ')
		bwt = BWT(string)
		print(bwt.transform())
	elif command == 'i_bwt':
		string = input('Please type string : ')
		i_bwt = BWT(string)
		print(i_bwt.inverse_transform())
	else:
		print('You\'ve typed wrond command\n Example command : python3 main.py {bwt - i_bwt} ')
	
if __name__ == '__main__':
	main()