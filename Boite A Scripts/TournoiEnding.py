##############################################################
#                                                            #
#                   Zone a ne pas toucher                    #
#                                                            #
##############################################################
import random
def randowaifumisateur(waifu:list)-> list:
    """
    Cette fonction prends en entrée une liste de waifu de longueure forcement paire
    et nous renvoie une liste de duo de waifu melangée
    """
    ran_waifu = []
    while len(waifu) != 0:
        waifu0 = waifu.pop(random.randint(0,len(waifu)-1))
        waifu1 = waifu.pop(random.randint(0,len(waifu)-1))
        ran_waifu.append([waifu0,waifu1])
    return ran_waifu

def purification(waifu):
    """
    Cette fonction prends en entrée une liste de duo de waifu et demande a 
    l'utilisateur quelles sont les waifu a SUPPRIMER pour purifier la liste
    des waifu inferieures 
    """
    ran_waifu = []
    for i in range(len(waifu)):
        print("on garde qui ? 0 pour ",waifu[i][0], "1 pour ",waifu[i][1])
        choix =  int(input("choix :" ))
        print(waifu[i][choix])
        ran_waifu.append(waifu[i][choix])
    pur_waifu = randowaifumisateur(ran_waifu)
    return pur_waifu

##############################################################
# c'est ici que tu touches 
round = 0


# il faut obligatoirement un nombre paire sinon
# cela ne marchera pas et il va te chier dessus
ending =["ending 1","ending 2","ending 3","ending 4"]

if round == 0:
    ending = randowaifumisateur(ending)
else:
    ending = purification(ending)

#######################################################
print(" ")
for i in range(len(ending)):
    print(ending[i][0]," vs ",ending[i][1])
print(" ")
print("a garder")
print(" ")
print(ending)
