def addtodico(string : str):
    if string in dico:
        dico[string] += 1
    else :
        dico[string] = 1 

history = open("/home/djalim/.zsh_history","r")
commandes = []
dico = {}
for ligne in history.readlines():
    try:
        commandes.append(ligne.split(';')[1])  
    except:
        commandes.append(ligne)

for i in commandes:
    try :
        if "\n" in i : i = i[:-1]
        addtodico(i.split(" ")[0])
    except :
        addtodico(i)

while len(dico.keys()) > 0 :
    maxi = 0
    keys = ""
    for i in dico.keys():
        if dico[i] > maxi : maxi, keys = dico[i], i
    print(dico[keys], " ", keys)
    del dico[keys]
