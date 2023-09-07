import fonctions as f

while True:
	nb = int(input("Saisir un nombre : "))
	nb2 = int(input("Saisir une deuxieme nombre : "))
	res = f.puissance(nb,nb2)
	print ("le carré de {} est {}".format(nb,nb*nb))
	print ("{} à la puissance {} vaut {}".format(nb,nb2,res))
