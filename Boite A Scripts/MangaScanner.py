#%%:
import pytesseract
import os
from multiprocessing.dummy import Pool as ThreadPool
from time import time
from datetime import datetime
pytesseract.pytesseract.tesseract_cmd = 'tesseract'

#------ fonctions -------
#
#



def est_ce_que_jy_suis(chemin):
    """
    Yop Djal du futur sa va?

    cette fonction parais chelou as fuck mais c'est parce que j'ai des contrainte
    en gros pour accelerer la vitesse de ce script j'ai opter pour du multithreading car
    python utilise un seul core, ouais c'est con, ducoup c'est pour sa que je doit
    crée un fontion avec un seul parametre et c'est aussi pour sa que je passe pas
    num et mot en parametre voilaaaaaaaaa
    """
    global num
    global mot
    print(num)
    num = num - 1
    oui = []
    if mot in pytesseract.image_to_string(str(chemin)):
        oui.append(chemin)
    return oui



#---------------------------------------#
#                                       #
#                  Main                 #
#                                       #
#---------------------------------------#


print("salam mec bienvenue dans probablent un des script les plus verbose que t'as jamais ecrit \nah et je suis case sensitive donc si t'oublie une majuscule ou si tu met une maj sa change tout \nalors on commence?")
path = str(input("chemin du dossier racine (les chemins relatifs marchent bg): "))
file_type = str(input("extention du fichier avec le point stp : "))
mot = str(input("le mot que tu cherche : "))
multithread = str(input("ah et bg tu veut du multi threading ou pas? [Non]/[Oui ou n'importe quoi sauf 'Non' :"))

if multithread == 'Non':
    multithread = False
else:
    multithread = True
    nb_de_core = int(input("combien de core tu veut utilisé bg? (en nombre entier stp) :"))

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if file_type in file:
            files.append(os.path.join(r, file))

num = len(files) # le nombre total pour un jolie countdown t'as cala

print("ouke alors j'ai ",num," pages a lire, c'est euu pas mal xD, je commence tt de suite")

debut = time()
now = datetime.now()
start = now.strftime("%H:%M:%S")
liste = []

if multithread == True :
    pool = ThreadPool(4)
    results = pool.map(est_ce_que_jy_suis, files) #cette ligne et la cause de tout mes malheurs
    pool.close()
    pool.join()
    for element in results:
        if len(element) != 0:
            liste.append(element)
    y = open(mot, "w")
    y.write(str(liste))
    y.close()

elif multithread == False :
    y = open(mot, "w")
    for element in files:
        if mot in pytesseract.image_to_string(str(element)) : 
            y.write(str(element)+"\n")
            liste.append(element)
        num = num - 1
        print(num)
    y.close()

fin = time()
now = datetime.now()
end = now.strftime("%H:%M:%S")
temps = fin - debut

print("yop voici la liste des fichier avec le mot: ",mot)
print(liste)      
print("en sah j'ai fini mec. en", temps,"secondes j'ai lu",len(liste),"page pour toi dit mrc fdp")
print("debut",start)
print("fin", end)


# %%
