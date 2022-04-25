import sql
from datetime import datetime

"""
Ce fichier contient les fonctions utilisées par le cote serveur du projet
"""

liste_spe_chr = ["'","#",","]
def date_heure(date):
    lol = ""
    for i in range(len(date)):
        if i != 10:
            lol += date[i]
        else:
            lol += " "
    return lol


############################################
#                                          #     
#           Connexion/Inscription          #
#                                          #
############################################

def connexion(pseudo_usr,password_hash):
    """
    Cette fonction execute la requete sql qui verifie que le pseudo reçu corresponds bien au hash associé
    en verifiant dans un premier lieu si le pseudo existe, sinon elle renvoie une erreur
    et si le hash corresponds au pseudo la fonction renvoie son user_id
    """
    print(sql.verification(pseudo_usr, password_hash))
    status = sql.verification(pseudo_usr, password_hash)
    if isinstance(status, int) :
        return {'status' : 'ok', 'user_id' : status} , 200
    else :
        return {'status' : status} , 500
    
def add_user(pseudo_usr,password_hash):
    """
    Cette fonction ajoute le pseudo (si le pseudo n'existe pas) et le mdp dans la table utilisateur et y associe un nouvel user_id
    """
    status = sql.ajouter_utilisateur(pseudo_usr,password_hash)
    if status == True:
        return {"status" :'ok'} , 200
    else:
        return {"status": status }  , 500 

############################################
#                                          #     
#             Gestion des amis             #
#                                          #
############################################

def add_friends(pseudo_usr,pseudo_friend):
    """
    Cette fonction permet d'ajouter le message envoyé par un utilisateur a la table message
    et en y ajoutant l'heure a la quelle le message a été reçu par le serveur
    """
    status = sql.ajouter_ami(pseudo_usr,pseudo_friend)
    if status == True:
        return {"status" :'ok'} , 200
    else:
        return {"status": status }  , 500 

def delete_friend(pseudo_usr,pseudo_friend):
    """
    """
    status = sql.retirer_ami(pseudo_usr,pseudo_friend)
    if status == True:
        return {"status" :'ok'} , 200
    else:
        return {"status" : status} , 500

def list_friends(user_id):
    """
    """
    status = sql.renvoyer_ami(user_id)
    if isinstance(status, list):
        return {'status': 'ok', 'friend_list' : status} , 200
    else:
        return {'status' : status} , 500
        
############################################
#                                          #     
#           Gestion des groupes            #
#                                          #
############################################

def add_user_in_group(pseudo_usr,group_name):
    """
    Cette fonction permet d'ajouter le message envoyé par un utilisateur a la table message
    et en y ajoutant l'heure a la quelle le message a été reçu par le serveur
    """
    status = sql.ajouter_utilisateur_groupe(pseudo_usr,group_name)
    if status == True:
        return {"status" :'ok'} , 200
    else:
        return {"status": status }  , 500 

def delete_user_in_group(pseudo_usr,group_name):
    """
    Cette fonction permet d'ajouter le message envoyé par un utilisateur a la table message
    et en y ajoutant l'heure a la quelle le message a été reçu par le serveur
    """
    status = sql.retirer_utilisateur_groupe(pseudo_usr,group_name)
    if status == True:
        return {"status" :'ok'} , 200
    else:
        return {"status": status }  , 500 

def list_usr_groups(user_id):
    """
    """
    status = sql.renvoyer_groupe(user_id)
    if isinstance(status, list):
        return {"status" : 'ok', 'group_list': status }, 200
    else:
        return {"status" : status }, 500

def list_usr_on_group(group_id):
    """
    """
    status = sql.renvoyer_utilisateurs_groupe(group_id)
    if isinstance(status, list):
        return {"status" : 'ok', 'group_list': status }, 200
    else:
        return {"status" : status }, 500

############################################
#                                          #     
#           Gestion des messages           #
#                                          #
############################################

def add_message_in_group(message,user_id,grp_id):
    """
    Cette fonction permet d'ajouter le message envoyé par un utilisateur a la table message
    et en y ajoutant l'heure a la quelle le message a été reçu par le serveur
    """
    message = message.replace("'",chr(1))
    status = sql.ajouter_message(message,date_heure(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')),int(user_id),int(grp_id))
    if status == True:
        return {"status": "ok"} ,200
    else:
        return {"status": status }, 500
    return


def delete_message(message_id):
    """
    Cette fonction permet de supprimer le message envoyé par un utilisateur 
    """
    status = sql.retirer_message(message_id)
    if status == True:
        return {"status" : "ok" }, 200 
    else:
        return {"status" : status }, 500
    return

def list_message(group_id):
    """
    """
    status = sql.renvoyer_message(group_id)
    if isinstance(status, list) :
        for messages in status:
            if chr(1) in messages[2]:
                messages[2] = messages[2].replace(chr(1), "'")
        return {"status" : 'ok', "message_list" : status}, 200
    else:
        return {"status" : status}, 500
    
############################################
#                                          #     
#           Gestion utilisateur            #
#                                          #
############################################

def changer_pseudo(usr_id, nouveau_pseudo):
    """
    """
    status = sql.changer_pseudo(usr_id, nouveau_pseudo)
    if status == True:
        return {"status" : "ok"}, 200
    else:
        return {"status" : status}, 500
    
def changer_mdp(usr_id, nouveau_mdp):
    """
    """
    status = sql.changer_mdp(usr_id, nouveau_mdp)
    if status == True:
        return {"status" : "ok"}, 200
    else:
        return {"status" : status}, 500
