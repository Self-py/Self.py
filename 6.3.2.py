def longest(my_list):
	"""
	This fucnction recives list of strings and returns the longest string from the list.
	:param my_list: list of strings
	:type my_list: list
	:return: the longest string from the list
	:rtype: str
	"""
	sorted_list = sorted(my_list, reverse=True, key=len)
	return sorted_list[0]