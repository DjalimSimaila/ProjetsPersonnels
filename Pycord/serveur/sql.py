import pymysql
import hashlib
import datetime

"""
Ce fichier se charge de la communication avec la base de donnée
"""
connexion = pymysql.connect(host = "lagrottedeneotaku.hopto.org", user = "Pycord", passwd = "f", database = "Pycord")
curseur = connexion.cursor()

def init():
    """
    Crée les tables dans la base de données sql
    :exemple:
        >>>curseur.execute("CREATE TABLE TABLE_TEST (id int(11) NOT NULL auto_increment, nom VARCHAR(20) NOT NULL, mot_de_passe BINARY(20) NOT NULL, PRIMARY KEY(id)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT = 'Une table test';")
    """
    curseur.execute("DROP TABLE IF EXISTS `APPARTIENT`,`MESSAGE`,`AMI`,`GROUPE`,`UTILISATEUR`")
    curseur.execute("CREATE TABLE `GROUPE` (grp_id INT NOT NULL AUTO_INCREMENT, nom_du_groupe VARCHAR(30) NOT NULL UNIQUE, PRIMARY KEY(grp_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT = 'La table groupe';")
    curseur.execute("CREATE TABLE `UTILISATEUR` (usr_id INT NOT NULL AUTO_INCREMENT, pseudo VARCHAR(30) NOT NULL UNIQUE, mdp_hash BINARY(255) NOT NULL, PRIMARY KEY(usr_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT = 'La table utilisateur';")
    curseur.execute("CREATE TABLE `MESSAGE` (mess_id INT NOT NULL AUTO_INCREMENT, message VARCHAR(8000) NOT NULL, heure DATETIME NOT NULL, usr_id INT NOT NULL, grp_id INT NOT NULL, PRIMARY KEY(mess_id), FOREIGN KEY(usr_id) REFERENCES UTILISATEUR(usr_id), FOREIGN KEY(grp_id) REFERENCES GROUPE(grp_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT = 'La table message';")
    curseur.execute("CREATE TABLE `AMI` (usr_id INT NOT NULL, usr_id_1 INT NOT NULL, FOREIGN KEY(usr_id) REFERENCES UTILISATEUR(usr_id), FOREIGN KEY(usr_id_1) REFERENCES UTILISATEUR(usr_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT = 'La table ami';")
    curseur.execute("CREATE TABLE `APPARTIENT` (grp_id INT NOT NULL, usr_id INT NOT NULL, FOREIGN KEY(grp_id) REFERENCES GROUPE(grp_id), FOREIGN KEY(usr_id) REFERENCES UTILISATEUR(usr_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT = 'La table appartient';")
    
def ajouter_utilisateur(pseudo, mdp_hash) :
    """
    Ajoute un utilisateur dans la table sql dédiée si il n'existe pas
    :usr_id: str
    :pseudo: str
    :mdp_hash: str
    """
    if isinstance(pseudo, str) and isinstance(mdp_hash, str) :
        if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE pseudo='{pseudo}'") == 0 :
            curseur.execute(f"INSERT INTO UTILISATEUR (pseudo, mdp_hash) VALUES ('{pseudo}',{int(mdp_hash, 16)})")
            connexion.commit()
            return True
        else :
            return 'Pseudo déjà utilisé'
    else :
        return 'Les variables doivent être des chaînes de caractère'

def ajouter_ami(pseudo, pseudo_ami) :
    """
    Ajoute les deux utilisateurs dans la table AMI si ils n'y sont pas déjà.
    :pseudo: str
    :pseudo_ami: str
    """
    if isinstance(pseudo, str) and isinstance(pseudo_ami, str) :
        if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE pseudo='{pseudo_ami}'") != 0 :
            if curseur.execute(f"SELECT * FROM AMI WHERE usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}') AND usr_id_1=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo_ami}')") == 0 and curseur.execute(f"SELECT * FROM AMI WHERE usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo_ami}') AND usr_id_1=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}')") == 0 :
                curseur.execute(f"INSERT INTO AMI (usr_id, usr_id_1) VALUES ((SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}'),(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo_ami}'))")
                connexion.commit()
                return True
            else :
                return f'Vous êtes déjà ami avec {pseudo_ami}'
        else :
            return f"L'utilisateur {pseudo_ami} n'existe pas"
    else :
        return 'Les variables doivent être des chaînes de caractère'

def retirer_ami(pseudo, pseudo_ami) :
    x=0
    if isinstance(pseudo, str) and isinstance(pseudo_ami, str) :
        if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE pseudo='{pseudo_ami}'") != 0 :
            if curseur.execute(f"SELECT * FROM AMI WHERE usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}') AND usr_id_1=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo_ami}')") != 0 :
                curseur.execute(f"DELETE FROM AMI WHERE usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}') AND usr_id_1=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo_ami}')")
                connexion.commit()
                x+=1
            if curseur.execute(f"SELECT * FROM AMI WHERE usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo_ami}') AND usr_id_1=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}')") != 0 :
                curseur.execute(f"DELETE FROM AMI WHERE usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo_ami}') AND usr_id_1=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}')")
                connexion.commit()
                x+=1
            if x > 0 :
                return True
            else : 
                return f'{pseudo} et {pseudo_ami} ne sont pas amis'
        else :
            return f"L'utilisateur {pseudo_ami} n'existe pas"
    else :
        return 'pseudo et pseudo_ami sont des str'
    
def ajouter_utilisateur_groupe(pseudo, nom_groupe):
    """
    Cette fonction execute la requette SQL permettant l'ajout d'un utilisateur dans un groupe, si le groupe n'existe pas, elle le crée et vérifie que l'utilisateur ajouté existe et n'appartient pas déjà au groupe.
    :nom_groupe: str
    :pseudo: str
    """
    if isinstance(pseudo, str) and isinstance(nom_groupe, str) :
        if curseur.execute(f"SELECT * FROM GROUPE WHERE nom_du_groupe='{nom_groupe}'") == 0 :
            curseur.execute(f"INSERT INTO GROUPE (nom_du_groupe) VALUES ('{nom_groupe}')")
            connexion.commit()
        if curseur.execute(f"SELECT * FROM APPARTIENT WHERE grp_id=(SELECT grp_id FROM GROUPE WHERE nom_du_groupe='{nom_groupe}') AND usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}')") == 0 :
            if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE pseudo='{pseudo}'") != 0 :
                curseur.execute(f"INSERT INTO APPARTIENT (grp_id, usr_id) VALUES ((SELECT grp_id FROM GROUPE WHERE nom_du_groupe='{nom_groupe}'), (SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}'))")
                connexion.commit()
                return True
            else :
                return "Cet utilisateur n'existe pas"
        else :
            return f"{pseudo} appartient déjà au groupe '{nom_groupe}'"
    else :
        return 'Les variables doivent être des chaînes de caractère'

def retirer_utilisateur_groupe(pseudo, nom_groupe):
    """
    Cette fonction execute la requette SQL permettant le retrait d'un utilisateur dans un groupe,
    Elle envoie ensuite un message dans le groupe informant le retrait de l'utilisateur 
    """
    if isinstance(pseudo, str) and isinstance(nom_groupe, str) :
        if curseur.execute(f"SELECT * FROM APPARTIENT WHERE grp_id=(SELECT grp_id FROM GROUPE WHERE nom_du_groupe='{nom_groupe}') AND usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}')") != 0 :
            if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE pseudo='{pseudo}'") != 0 :
                curseur.execute(f"DELETE FROM APPARTIENT WHERE grp_id=(SELECT grp_id FROM GROUPE WHERE nom_du_groupe='{nom_groupe}') AND usr_id=(SELECT usr_id FROM UTILISATEUR WHERE pseudo='{pseudo}')")
                connexion.commit()
                if curseur.execute(f"SELECT * FROM APPARTIENT WHERE grp_id=(SELECT grp_id FROM GROUPE WHERE nom_du_groupe='{nom_groupe}')") == 0 :
                    curseur.execute(f"DELETE FROM GROUPE WHERE nom_du_groupe = '{nom_groupe}'")
                connexion.commit()
                return True
            else :
                return "Cet utilisateur n'existe pas"
        else :
            return f"{pseudo} n'appartient pas au groupe '{nom_groupe}'"
    else :
        return 'Les variables doivent être des chaînes de caractère'
    
def ajouter_message(message, datetime, usr_id, grp_id) :
    """
    Enregistre un mesage dans la table sql
    :message: str
    :datetime: str, 'AAAA-MM-JJ HH:MM:SS'
    :usr_id: int
    :grp_id: int
    """
    if isinstance(message, str) and isinstance(datetime, str) and isinstance(usr_id, int) and isinstance(grp_id, int) :
        if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE usr_id={usr_id}") != 0 and curseur.execute(f"SELECT * FROM GROUPE WHERE grp_id={grp_id}") != 0 :
            curseur.execute(f"INSERT INTO MESSAGE (message, heure, usr_id, grp_id) VALUES ('{message}', '{datetime}', {usr_id}, {grp_id})")
            connexion.commit()
            return True
        else :
            return "L'utilisateur ou le groupe n'existe pas"
    else :
        return 'Les variables ne sont pas au bon format'
    
def retirer_message(mess_id) :
    if curseur.execute(f"SELECT * FROM MESSAGE WHERE mess_id={mess_id}") != 0 :
        curseur.execute(f"DELETE FROM MESSAGE WHERE mess_id={mess_id}")
        connexion.commit()
        return True
    else :
        return "Le message n'existe pas"

def verification(pseudo, mdp_hash) :
    "Verifie que le pseudo existe, et que le mdp correspond au hash. Renvoie le user_id"
    if isinstance(pseudo, str) and isinstance(mdp_hash, str) :
        if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE pseudo='{pseudo}' AND mdp_hash={int(mdp_hash,16)}") != 0 :
            usr_id = curseur.fetchone()
            usr_id = usr_id[0]
            return usr_id
        else :
            'Le mot de passe ou le pseudo est incorrect'
    else :
        return 'Les variables doivent être des chaînes de caractère'
    
def renvoyer_groupe(usr_id) :
    "Renvoie la liste des couples (nom,grp_id) des groupes auquel appartient l'utilisateur"
    if curseur.execute(f"SELECT nom_du_groupe FROM GROUPE JOIN APPARTIENT ON usr_id={usr_id} and GROUPE.grp_id=APPARTIENT.grp_id") != 0 :
        tuple_grp = curseur.fetchall()
        curseur.execute(f"SELECT grp_id FROM APPARTIENT WHERE usr_id={usr_id}")
        tuple_id_grp = curseur.fetchall()
        liste_grp = []
        for i in range(len(tuple_grp)) :
            liste_grp.append((tuple_grp[i][0],tuple_id_grp[i][0]))
        return liste_grp
    else :
        return "L'utilisateur n'appartient à aucun groupe"
        
def renvoyer_ami(usr_id) :
    "Renvoie la liste des pseudos des amis de l'utilisateur"
    liste_ami = []
    if curseur.execute(f"SELECT pseudo FROM UTILISATEUR JOIN AMI ON usr_id_1={usr_id} AND UTILISATEUR.usr_id=AMI.usr_id") != 0 :
        tuple_ami = curseur.fetchall()
        for element in tuple_ami :
            liste_ami.append(element[0])
    if curseur.execute(f"SELECT pseudo FROM UTILISATEUR JOIN AMI ON AMI.usr_id={usr_id} AND UTILISATEUR.usr_id=usr_id_1") != 0 :
        tuple_ami = curseur.fetchall()
        for element in tuple_ami :
            liste_ami.append(element[0])
    if liste_ami != [] :
        return liste_ami
    else :
        return "L'utilisateur n'a pas d'ami"
    
def renvoyer_message(grp_id) :
    liste_message = []
    if curseur.execute(f"SELECT * FROM MESSAGE WHERE grp_id={int(grp_id)}") != 0 :
        tuple_message = curseur.fetchall()
        for element in tuple_message :
            curseur.execute(f"SELECT pseudo FROM UTILISATEUR WHERE usr_id={element[3]}")
            pseudo = curseur.fetchall()[0][0]
            liste_message.append([element[0], pseudo, element[1], str(element[2]), element[3], element[4]])
        return liste_message
    else :
        return 'Aucun message'
    
def renvoyer_utilisateurs_groupe(grp_id) :
    liste_utilisateurs = []
    if curseur.execute(f"SELECT pseudo FROM UTILISATEUR JOIN APPARTIENT ON grp_id={grp_id} and UTILISATEUR.usr_id=APPARTIENT.usr_id") != 0 :
        tuple_utilisateurs = curseur.fetchall()
        for element in tuple_utilisateurs :
            liste_utilisateurs.append(element[0])
        return liste_utilisateurs
    else :
        return "Ce groupe n'existe pas"
    
    
def changer_pseudo(usr_id : int, nouveau_pseudo : str) :
    "Change le pseudo d'un utilisateur si il existe"
    if isinstance(usr_id, int) and isinstance(nouveau_pseudo, str) :
        if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE usr_id={usr_id}") != 0 :
            curseur.execute(f"UPDATE UTILISATEUR SET pseudo='{nouveau_pseudo}' WHERE usr_id={usr_id}")
            connexion.commit()
            return True
        else :
            return "Cet utilisateur n'existe pas"
    else : 
        return "Les variables ne sont pas au bon format"
    
def changer_mdp(usr_id : int, nouveau_mdp : str) :
    "Change le mot de pase d'un utilisateur si il existe"
    if isinstance(usr_id, int) and isinstance(nouveau_mdp, str) :
        if curseur.execute(f"SELECT * FROM UTILISATEUR WHERE usr_id={usr_id}") != 0 :
            curseur.execute(f"UPDATE UTILISATEUR SET mdp_hash='{nouveau_mdp}' WHERE usr_id={usr_id}")
            connexion.commit()
            return True
        else :
            return "Cet utilisateur n'existe pas"
    else : 
        return "Les variables ne sont pas au bon format"
