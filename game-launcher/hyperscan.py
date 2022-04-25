import gamedb
import os

Gamedb = gamedb.Game_database()
gamedir= "/run/media/djalim/HDD/ArcheDeNeo/Games"

def scan_moi_ce_dossier_bg(dossier: str):
    """
    Cette fonction scan le dossier de jeu en paramettre et te guide comme un assisté a la creation d'une jolie
    base de donnée sous forme de dict dont la clé est le nom du jeu et la valeur la commande a executer
    simùple, basique et terriblement swag
    
    elle retourne rien car elle a ete concue en stand alone, je pense que je vais lui donner son propre fichier
    en vrai
    
    """
    liste_dossier = [f for f in os.listdir(dossier) if not os.path.isfile(os.path.join(dossier,f))]
    print(
        """
        Salam bg, on va scanner et créer une database ensemble comme deux frere
        """
    )
    s= ""
    for i in Gamedb.donne_moi_la_db().keys():
        s += i + "\n"
    print("jeux installés :\n" + s)
    print("")
    for jeux in liste_dossier:
        if jeux not in Gamedb.donne_moi_la_db():
            print("Est ce que " + jeux + " est un jeu que tu veux ajouter a la base de donnée?")
            rep = input("[oui],[non],[quitte]: ")
            if rep == "oui":
                print('hop')
                liste_exe = []
                for r,d,f in os.walk(os.path.join(dossier,jeux)):
                    for fichier in f:
                        if '.exe' in fichier: liste_exe.append((fichier,os.path.join(r,fichier)))
                j = 0
                for i in liste_exe:
                    print("")
                    print(str(j) +" "+i[0] )
                    j += 1
                print("quel est le bon exe?")
                rep = input('index: ')
                if rep == 'quit':
                    pass
                else:
                    rep = int(rep)
                    chemin_exe = liste_exe[rep][1]
                    Gamedb.ajoute_ce_jeu_dans_la_db_bg(jeux,chemin_exe)
            elif rep == "quit":
                return
            else:
                pass
    return

scan_moi_ce_dossier_bg(gamedir)
