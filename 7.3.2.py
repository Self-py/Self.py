def check_win(secret_word, old_letters_guessed):
	"""
	the fucnction returns "True" if all of the letters in the secret word are in the old letters guessed list. else, returns "False".
	:param secret_word: the final word
	:param old_letters_guessed: list of the old letters guessed
	:type secret_word: str
	:type old_letters_guessed: list
	:return: True or False
	:rtype: str
	"""
	true_false_str = ""
	for letter in secret_word:
	    if letter in old_letters_guessed:
	        true_false_str += "True"
	    else:
	        true_false_str += "False"

	if "False" in true_false_str:
		return False
	else:
		return True