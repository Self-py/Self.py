def show_hidden_word(secret_word, old_letters_guessed):
	"""
	Show the status of the hidden word.
	:param secret_word: the final word
	:param old_letters_guessed: the old letters guessed
	:type secret_word: str
	:type old_letters_guessed: list
	:return: the final word
	:rtype: str
	"""
	secret_word_progress = []
	for letter in secret_word:
		if letter in old_letters_guessed:
			secret_word_progress.append(letter + " ")
		else:
			secret_word_progress.append("_ ")
	result = ''.join(secret_word_progress)
	return result[:-1]