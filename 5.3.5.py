def distance(num1, num2, num3):
	A = (abs(abs(num2) - abs(num1)) == 1) or (abs(abs(num3) - abs(num1)) == 1)
	B = ((abs(abs(num2) - abs(num1)) > 1) and (abs(abs(num2) - abs(num3)) > 1)) or ((abs(abs(num3) - abs(num1)) > 1) and (abs(abs(num3) - abs(num2)) > 1))
	if A and B:
		return True
	else:
		return False