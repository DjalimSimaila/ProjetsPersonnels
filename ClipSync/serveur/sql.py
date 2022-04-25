import pymysql
import hashlib
import datetime

"""
Ce fichier se charge de la communication avec la base de donnée
"""
connexion = pymysql.connect(host = "lagrottedeneotaku.hopto.org", user = "clipsync", passwd = "DOHG8FYJGYOFGORKG21RGN82FJIG", database = "clipsync")
cursor = connexion.cursor()


def getIdDev(token) -> str:
    request = "SELECT id_dev FROM devices WHERE token = %s;"
    cursor.execute(request,(token))
    id_dev = cursor.fetchone()
    return id_dev

def getIdUser(token) -> str:
    request = "SELECT id_user FROM devices WHERE token = %s;"
    cursor.execute(request,(token))
    id_user = cursor.fetchone()
    return id_user

def getLatest(token) -> list:
    id_user = getIdUser(token)
    request = "SELECT last_clip FROM users WHERE id_user = %s;"
    cursor.execute(request,(id_user))
    latest = cursor.fetchone()
    return latest

def getTrueLatest(token) -> list:
    id_user = getIdUser(token)
    request = "SELECT max(id_clip) FROM clipboard WHERE id_dev in (SELECT DISTINCT id_dev FROM device WHERE id_user = %s)"
    cursor.execute(request,(id_user))
    latest = cursor.fetchone()
    return latest

def setLatest(token,timestamp,value):
    """
    """
    # id_dev, timestamp, value
    id_dev = getIdDev(token)
    insert_request ="INSERT INTO clipboards( %s, %s, %s);"
    cursor.execute(insert_request,(id_dev,timestamp,value))
    last_clip = getTrueLatest(token)
    id_user = getIdUser(token)
    update_request ="UPDATE users SET last_clip=%s WHERE id_user =%s;"
    cursor.execute(update_request(last_clip,id_user))




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
