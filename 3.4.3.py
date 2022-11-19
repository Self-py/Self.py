string = input("Please enter a string: ")
print(string[:len(string) // 2].lower() + string[len(string) // 2:].upper())