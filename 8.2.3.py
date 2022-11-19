def mult_tuple(tuple1, tuple2):
	"""
	Builds all possible couples of the given 2 tuples
	:params: tuple1, tuple2: input touples
    :return: tuple contains all the couples. Order not mandatory
    :rtype: tuple
    """
	list = []
	for i in tuple1:
		for b in tuple2:
			list.append((i, b))
			list.append((b, i))
	return tuple(list)