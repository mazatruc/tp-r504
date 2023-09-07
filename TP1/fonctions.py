def puissance(a,b):
	if not type(a) is int :
		if not type(b) is int:
			raise TypeError("only integers are allowed")

	if a == 0:
		return 1

	rep = abs(-a)
	for cheh in range (1,b):
		rep = rep*a

	return abs(rep)
