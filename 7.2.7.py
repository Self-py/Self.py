def arrow(my_char, max_length):
	"""
	Draw an errow-shape, built of the input character.
    :param my_char: the chararter to nuild the errow with
    :param max_length: length of the longest raw in the shape
    :type my_char: character
    :type max_length: int
    :return: the errow shape
    :rtype: list
	"""
	my_str = ""
	i = 1
	for num in range(max_length):
		my_str += (my_char * i)
		my_str += "\n"
		i += 1
	i -= 2
	for num in range(max_length - 1):
		my_str += (my_char * i)
		my_str += "\n"
		i -= 1
	return my_str[:-1]