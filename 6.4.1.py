def check_valid_input(letter_guessed, old_letters_guessed):
	"""
	this function receives a input and checks if the input is proper. If the input has more than one Character, or the input has a sign that is not an English letter, than the function will rerutn "False", also if the letter is already gessed. But if the input has only one English letter, the function will rerutn "True".
	:param letter_guessed: the input
	:param old_letters_guessed: letters that have been already gessed
	:return: "True" or "False"
	:rtype: str
	"""
	if len(letter_guessed) > 1:
		return False
	if not letter_guessed.isalpha():
		return False
	if ((letter_guessed.lower()) or (letter_guessed.upper())) in old_letters_guessed:
		return False
	else:
		return True