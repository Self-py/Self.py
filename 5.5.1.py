def is_valid_input(letter_guessed):
	"""
	this function receives a input and checks if the input is proper. If the input has more than one Character, or the input has a sign that is not an English letter, than the function will rerutn "False". But if the input has only one English letter, the function will rerutn "True".
	:param letter_guessed: the input
	:return: "True" or "False"
	:rtype is_valid_input: str
	"""
	if len(letter_guessed) > 1:
		return False
	if not letter_guessed.isalpha():
		return False
	else:
		return True

def main():
	# Call the function is_valid_input
    is_valid_input("a")

if __name__ == "__main__":
    main()