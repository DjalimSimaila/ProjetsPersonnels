nom = "test.yaml"

def yamlParser(nom):
	"""
	"""
	fichier = open(nom,"r")
	listeLigne = []
	listeClef = []
	listeValeur = []
	for ligne in fichier.readlines():
		if '#' in ligne:
			pass
		ligne = ligne[:-1]
		listeLigne.append(ligne.split(' : '))
	for i in listeLigne:
		listeClef.append(i[0])
		listeValeur.append(i[1])
	fichier.close()
	return listeClef,listeValeur


def findNextKey(fichier,debut,indentation):
	"""
	"""
	i = debut
	while True:
		if i < len(fichier) and indentation * '\t' in  fichier[i]:
			i += 1
		else:
			return i

def underparser(fichier,debut,fin,indent):
	"""
	"""
	dico = {}
	i = debut
	while(i < fin):
		ligne = fichier[i]
		if '#' in ligne:
			i+=1
			continue
		ligne = ligne[:-1].split(':')
		print(ligne)
		if ligne[1] == '':
			sousFin = findNextKey(fichier,i+1,indent)
			dico[ligne[0]] = underparser(fichier,i+1,sousFin,indent + 1)
			i = sousFin
		else:
			dico[ligne[0]] = ligne[1]
			i += 1
	return dico


fichier = open(nom,"r")
listLigne = []
for i in fichier.readlines():
	listLigne.append(i)
config = underparser(listLigne,0,len(listLigne),0)
print(config)
fichier.close()
