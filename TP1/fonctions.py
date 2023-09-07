def puissance(a,b):
	if not type(a) is int :
		if not type(b) is int:
			raise TypeError("only integers are allowed")

	if a == 0 and b == 0:
		return 1

	if b == 0 :
		if a <= 0:
			return -1
		else:
			return 1

	rep = abs(-a)
	if b <= 0:
		c = -1
		mn = abs(b)
	else:
		c = 1
		mn = 1

	for cheh in range (mn,b,c):
		rep = rep*a

	return rep
