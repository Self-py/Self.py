word = input("Enter a word: ").replace(" ", "")
if (word.lower() == word.lower()[::-1]):
	print("OK")
else:
	print("NOT")