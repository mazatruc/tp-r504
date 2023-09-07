def puissance2(a,b):
	if not type(a) is int :
		if not type(b) is int:
			raise TypeError("only integers are allowed")
#conditions des cas 0 :

	if a == 0 and b == 0:
		return 1

	if b == 0:
		if a <= -1:
			return -1
		else:
			return 1

	reponse = abs(-a)

#conditions des puissances négatives ou positives :

	if b <= 0: #si b est négatif le pas est de -1 et la boucle commence à b positif
		pas = -1
		mn = abs(b)
	else: #si b est positif le pas est de 1 et la boucle commence à 1
		pas = 1
		mn = 1

	for cheh in range (mn,b,pas):
		reponse = reponse*a

	return reponse
def puissance(x,n):
	sortie = 1
	if x == 0 and n != 0:
		return 0
	for cheh in range(n):
		sortie = sortie*x
	return sortie
