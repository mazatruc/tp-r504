def puissance(a,b):
	if not type(a) is int :
		if not type(b) is int:
			raise TypeError("only integers are allowed")
	return a**b
