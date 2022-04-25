import os
import ast

"""
{
    'jeu1': {"cmd" :'wine' , "chemin": '/chemin/du/jeu1.exe', 'variables' :'__NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia ,"status" : "works" },
    'jeu2': {"cmd" :'wine' , "chemin": '/chemin/du/jeu2.exe', 'variables' : " ", "status" : "doesnt work" },
    'jeu3': {"cmd" :'wine' , "chemin": '/chemin/du/jeu3.exe', 'variables' : " ", "status" : "untested" }
}

"""
#############################################################
#                                                           #
#                 Fonctions that reads the db               #
#                                                           #
#############################################################

def ouvre_moi_la_data_base() -> dict:
    """
    Cette fonction porte bien son nom, car elle lit le fichier contenant la base de données des jeux
    et la retourne sous la forme d'un joli poti dict a la python commme on les aimes
    
    exemple:
        >>> ouvre_moi_la_data_base()
        {"Pussy Slayer Simulator 2069": 'prime-run wine /run/media/god/TheVault/Games/PDS/pds.exe'}
    
    :return: la base de donnée
    :r type: dict
    
    """
    if not os.path.isfile("./game_db.db"):
        os.system("touch ./game_db.db")
        os.system("echo {} >> ./game_db.db")
    game_db_file = open('game_db.db','r')
    game_db = ast.literal_eval(game_db_file.read())
    game_db_file.close()
    return game_db

def lance_moi(jeu : str):
    """
    Bon c'est la fonction la plus importante de ce fucking script, c'est celle qui lance les jeux de la db
    elle se contente juste de prendre les Variables d'environement, la commande et le chemin du jeu de les
    lancer dans shell

    exemple:
        >>>lance_moi('Pussy Slayer Simulator 2069')
        (True, "it has been launched, i guess?")
    
    :jeu: le nom du jeu
    :jeu type: str
    :return: la base de donnée
    :r type: dict

    """
    db = ouvre_moi_la_data_base()
    commande = db[jeu]['variables']+ " " +db[jeu]['cmd'] 
    os.system(commande)
    return (True, "it has been launched, i guess?")


#############################################################
#                                                           #
#               Fonctions that writes into de db            #
#                                                           #
#############################################################


def sauvegarde_la_db_bg(game_db : dict)-> tuple:
    """
    Une autre fonction qui porte bien son nom, cette fonction prends le dict python en parametre et
    ECRASE le fichier base de donnée avec son nouveau contenu, mais on fait quand meme un backup car on
    est jamais trop prudant wola
    
    exemple si inchallah tout ce passe bien:
        >>> sauvegarde_la_db_bg()
        return (True, "C'est bon c'est sauvegardé bg")
    
    :game_db: la base de donnée bg
    :game_db type: dict
    :return: code erreur + message
    :r type: tuple    

    """
    if os.path.isfile("./game_db.bak"):
        os.system("rm -f ./game_db.bak")
        os.system("cp ./game_db.db game_db.bak")
    else:
        os.system("cp ./game_db.db game_db.bak")
    os.system("rm -f ./game_db.db")
    game_db_file = open('game_db.db','w')
    game_db_file.write(str(game_db))
    game_db_file.close()
    return (True, "C'est bon c'est sauvegardé bg")

def ajoute_ce_jeu_dans_la_db_bg(jeu :str ,chemin_exe: str) -> tuple:
    """
    Dans le cas ou toi pas savoir lire, cette fonction ajoute le jeu susnommé dans laditte
    base de donnée, enfin, si le jeu n'y est pas deja sinon cette focntion va juste insulter tes morts
    cette fonction verifie aussi si le jeux existe, se serait chiant de se retrouver avec des fichier fantomes  
    
    exemple:
        >>> ajoute_ce_jeu_dans_la_db_bg('osu!','/run/media/god/TheVault/games/Osu/osu!.exe')
        (False, "wsh bg, je connais ce jeu, ca veut dire qu'il est dans la bbd enculé")
        >>> ajoute_ce_jeu_dans_la_db_bg('Porkyman Breedable edition HD','/run/media/god/TheVault/games/PKMNBEHD/Breed.exe')
        (True, "Ajouté, clean propre et carré dans l'axe")

    :jeu: le nom du jeu 
    :jeu type: str
    :chemin_exe: le path to the jeu 
    :chemin type: str 
    :return: code erreur + message
    :r type: tuple  
    """
    db = ouvre_moi_la_data_base()
    if jeu in db.keys():
        return (False, "wsh bg, je connais ce jeu, ca veut dire qu'il est dans la bdd enculé")
    elif not os.path.isfile(chemin_exe):
        return  (False, 'Apres les amis imaginaire voici les jeux imaginaire, ton jeu il existe pas bg')
    else:
        try:
            db[jeu] = {}
            db[jeu]['cmd'] = "wine"
            db[jeu]['path'] = chemin_exe 
            db[jeu]['variable'] = ""
            db[jeu]['status'] = 'untested'
        except:
            return (False, "ouké alors, je sais pas pk mais je peux pas ajouter le jeu dans la bdd")
        else:
            sauvegarde_la_db_bg(db)
            return (True, "Ajouté, clean propre et carré dans l'axe")

def modifie_la_commande_de(jeu: str ,cmd :str) -> tuple:
    """
    Tiens tiens tiens, encore une fonction qui porte bien son nom, cette fonction prends le jeu en parametre et la commande a cote
    et ECRASE betement la commande dans la base de donnée.

    exemple:
        >>> modifie_la_commande_de("Pussy Slayer Simulator 2069","wine")
    (True, "Hopla, c'est modifié, c'est pas beau la technologie ?")
    
    
    :jeu: le nom du jeu 
    :jeu type: str
    :cmd: la commande a faire pour lancer le jeu
    :cmd type: str
    :return: code erreur + message
    :r type: tuple
    
    """
    db = ouvre_moi_la_data_base()
    db[jeu]["cmd"] = cmd
    sauvegarde_la_db_bg(db)
    return (True, "Hopla, c'est modifié, c'est pas beau la technologie ?")

def modifie_les_variables_de(jeu: str ,ve :str) -> tuple:
    """
    copiée de celle juste au dessus

    Tiens tiens tiens, encore une fonction qui porte bien son nom, cette fonction prends le jeu en parametre et la commande a cote
    et ECRASE betement la commande dans la base de donnée.

    exemple:
        >>> modifie_la_commande_de("Pussy Slayer Simulator 2069","wine")
    (True, "Hopla, c'est modifié, c'est pas beau la technologie ?")
    
    
    :jeu: le nom du jeu 
    :jeu type: str
    :cmd: la commande a faire pour lancer le jeu
    :cmd type: str
    :return: code erreur + message
    :r type: tuple
    
    """
    db = ouvre_moi_la_data_base()
    db[jeu]["variables"] = ve
    sauvegarde_la_db_bg(db)
    return (True, "Hopla, c'est modifié, c'est pas beau la technologie ?")

def attribue_la_gtx_a(jeu: str):
    """
    """
    db = ouvre_moi_la_data_base()
    db[jeu]['variables'] += " __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia"
    sauvegarde_la_db_bg(db)
    return (True, "La puissance de la team green a été attribué a ce jeu, puisse-t-il s'en servir a bon escient")

def retire_la_gtx_a(jeu:str):
    """
    """
    a_supp = ["__NV_PRIME_RENDER_OFFLOAD=1", "__VK_LAYER_NV_optimus=NVIDIA_only", "__GLX_VENDOR_LIBRARY_NAME=nvidia"]
    db = ouvre_moi_la_data_base()
    liste_ve = db[jeu]['variables']
    ve = ""
    for i in liste_ve:
        if i in a_supp: liste_ve.pop(liste_ve.index(i))
        else: ve += i +" "
    db[jeu]['variables'] = ve
    sauvegarde_la_db_bg(db)
    return (True, "Addios team green")

def change_le_status_de(jeu: str, valeur: (int or str) =  0 )-> tuple:
    """
    """
    db = ouvre_moi_la_data_base()
    status_int = {0: "untested", 1 : "works", 2 : "doesn't work"}
    status_str = ("untested","works","doesn't work") 
    if valeur in status_int.keys():
        db[jeu]['status'] = status_int[valeur]
        sauvegarde_la_db_bg(db)
        return (True, "GG voila un nouveau status qui fait plaiz, ou pas .w.")
    elif valeur in status_str:
        db[jeu]['status'] = valeur
        sauvegarde_la_db_bg(db)
        return (True, "GG voila un nouveau status qui fait plaiz, ou pas .w.")
    else:
        return (False, " Bro donne moi un vrai status je suis sensé faire quoi avec ta merde?") 

def renomme(jeu :str, nouveau_nom :str) -> tuple:
    """
    Cette fonction au nom sobre mais fichtrement explicite renomme le jeu selectioné, s'il est present dans la base de donnée,
    vers sa nouvelle valeur, si celle ci n'est pas presente dans la base de donnée
    
    exemple:
        >>> renomme("Pussy Slayer Simulator 2069","Pussy Slayer Simulator 42069")
        (True, "C'est bon t'as un magnifique nouveau nom") 
    
    :return: code erreur + message
    :r type: tuple
    """
    db = ouvre_moi_la_data_base()
    if jeu not in db.keys():
        return (False,'je connais pas ce jeu bg')
    elif nouveau_nom not in db.keys():
        db[nouveau_nom] = db[jeu]
        sauvegarde_la_db_bg(db)
        return (True, "C'est bon t'as un magnifique nouveau nom")
    return (False, "ce message n'est pas sensé pouvoir etre atteind wtf")
