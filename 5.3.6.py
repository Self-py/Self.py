def fix_age(age):
	return 0
def filter_teens(a=13, b=13, c=13):
	if (a >= 13 and  a <= 14) or (a >= 17 and a <= 19):
		a = fix_age(a)
	if (b >= 13 and  b <= 14) or (b >= 17 and b <= 19):
		b = fix_age(b)
	if (c >= 13 and  c <= 14) or (c >= 17 and c <= 19):
		c = fix_age(c)
	return a + b + c