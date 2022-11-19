def squared_numbers(start, stop):
	"""
	this function recives two integers and returns a list with all of the squares of the numbers between the two numbers, including the the squares of the two numbers.
	:param start: an integer
	:param stop: an integer
	:type start: int
	:type stop: int
	:return: a list with all of the squares of the numbers between the two numbers
	:rtype: list
	"""
	squared = []
	while start <= stop:
		start += 1
		squareing = (start - 1) ** 2
		squared.append(squareing)
	return squared