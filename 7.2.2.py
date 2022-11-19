def numbers_letters_count(my_str):
		"""
		This fucnction recives a string. The fucnction returns a list which the first item that in her is the number of the numbers in the string, and the second item  that is in the list is the numbers of every digit that is not a number.
		:param my_str: a string
		:type my_str: str
		:return: a list
		:rtype: list
		"""
		sum_digits = 0
		sum_letters = 0
		for digit in my_str:
			if digit.isdigit(): 
				sum_digits += 1
			else: 
				sum_letters += 1
		return [sum_digits, sum_letters]