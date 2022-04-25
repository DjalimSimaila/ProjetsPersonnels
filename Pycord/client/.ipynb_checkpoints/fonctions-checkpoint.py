import requests
import json
import hashlib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

############################################
#                                          #     
#               Configuration              #
#                                          #
############################################

# Les parametres ip et ports sont à configurer vers l'ip ou le domaine qui heberge le serveur
ip = '51.210.46.79'
port = "5016"

############################################
#                                          #     
#               Experiemental              #
#                                          #
############################################



def test():
    """
    """
    test = requests.post("https://"+ip+":"+port+"/test/", data={})
    if contenu['status'] != 'ok':
        print('ya une erreur bg')
        return
    else:
        reponse = json.loads(test.content.decode('utf-8'))
        return reponse

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################


def requete(chemin: str, données: dict ) -> requests.models.Response:
    """
    Fonction qui effectue les requetes POST au serveur
    
    :param chemin: chemin de la requete
    :type chemin: Chaine de charactere - str
    :param données: Les données a transmetre au serveur
    :type données: Dictionaire - dict
    :return: La reponse du serveur
    :r type: reponse request - requests.models.Response
    
    exemple:
    
    >>> test = requete('/get_friend_list/',{'user_id':user_id})
    >>> test
    <Response [200]>
    
    """
    
    try:
        status = requests.post("https://"+ip+":"+port+chemin, data=données,verify=False)
    except:
        return False , "Erreur: Connection impossible ou perdue"
    else:
        return status 


############################################
#                                          #     
#           Connexion/Inscription          #
#                                          #
############################################


def connexion(pseudo:str,mot_de_passe:str) -> tuple:
    """
    Cette fonction envoie au serveur le pseudonyme et le hash du mot de passe de l'utilisateur
    et retourne un tuple contant l'user id si l'utilisateur existe
    
    :param pseudo: Pseudonyme de l'utilisateur
    :type pseudo: Chaine de charactere - str
    :param mot_de_passe: mot de passe de l'utilisateur
    :type mot_de_passe: Chaine de charactere - str
    :return: Tuple de reponse
    :r type: Tuple - tuple
    
    exemple:
    >>> test = connexion('test','test')
    >>> test
    (True,'ok',0)
    
    """
    mot_de_passe = hashlib.sha256(mot_de_passe.encode("utf-8")).hexdigest()
    connexion = requete("/connexion/",{'pseudo':pseudo,'mot_de_passe':mot_de_passe})
    contenu = json.loads(connexion.content.decode('utf-8'))
    if contenu['status'] != 'ok':
        return False, 'Erreur: Identifiants incorects ou inexistants'
    else:
        return True, contenu['status'], contenu['user_id']


def inscription(pseudo:str ,mot_de_passe:str ,mot_de_passe_confirmation:str):
    """
    Cette fonction compare les deux mots de passes mit en parametre
    puis envoie au serveur le pseudonyme et le hash du mot de passe de l'utilisateur
    et indique si le compte a ete crée, et si non les raison pourquoi
    
    :param pseudo: Pseudonyme de l'utilisateur
    :type pseudo: Chaine de charactere - str
    :param mot_de_passe: mot de passe de l'utilisateur
    :type mot_de_passe: Chaine de charactere - str
    :param mot_de_passe_confirmation: confirmation du mot de passe de l'utilisateur
    :type mot_de_passe_confirmation: Chaine de charactere - str
    :return: Tuple de reponse
    :r type: Tuple - tuple
    
    exemple:
    >>> test = inscription('test','test','test')
    >>> test
    (True,'ok')
    
    """
    if mot_de_passe != mot_de_passe_confirmation:
        return False, "Erreur: les mots de passe ne correspondent pas"
    else:
        mot_de_passe = hashlib.sha256(mot_de_passe.encode("utf-8")).hexdigest()
        compte = requete("/add_user/",{'pseudo':pseudo,'mot_de_passe':mot_de_passe})
    print(compte)
    contenu = json.loads(compte.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True , contenu['status']
    else:
        return False, contenu['status'] 

############################################
#                                          #     
#           Gestion des groupes            #
#                                          #
############################################

def ajouter_dans_groupe(pseudo:str ,nom_du_groupe:str):
    """
    Cette fonction ajoute un utilisateur dans un groupe
    
    :param pseudo: Pseudonyme de l'utilisateur
    :type pseudo: Chaine de charactere - str
    :param nom_du_groupe: Nom du groupe ou ajouter l'utilisateur
    :type nom_du_groupe: Chaine de charactere - str
    :return: Tuple de reponse
    :r type: Tuple - tuple
    
    exemple:
    >>>
    
    """
    ajout = requete('/add_to_group/',{'pseudo':pseudo,'group_name':nom_du_groupe})
    contenu = json.loads(ajout.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True , contenu['status']
    else:
        return False, contenu['status']

def retirer_dans_groupe(pseudo,nom_du_groupe):
    retrait = requete('/del_from_group/',{'pseudo':pseudo,'group_name':nom_du_groupe})
    contenu = json.loads(retrait.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True , contenu['status']
    else:
        return False, contenu['status']

def charger_groupe(user_id):
    liste = requete('/get_group_list/',{'user_id': user_id})
    contenu = json.loads(liste.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True, contenu['status'], contenu['group_list']
    else:
        return False, contenu['status']
    
def charger_utilisateur_groupe(group_id):
    liste = requete('/get_group_user_list/',{'group_id': group_id})
    contenu = json.loads(liste.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True, contenu['status'], contenu['group_list']
    else:
        return False, contenu['status']

############################################
#                                          #     
#             Gestion des amis             #
#                                          #
############################################
def ajouter_amis(pseudo, pseudo_ami):
    """
    """
    ajout = requete('/add_to_friends/',{'pseudo': pseudo, "pseudo_ami" : pseudo_ami})
    contenu = json.loads(ajout.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True , contenu['status']
    else:
        return False, contenu['status']

def retirer_amis(pseudo,pseudo_ami):
    """
    """
    retrait = requete('/del_from_friend/',{'pseudo': pseudo, 'pseudo_ami': pseudo_ami})
    contenu = json.loads(retrait.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True , contenu['status']    
    else:
        return False, contenu['status']

def charger_amis(user_id):
    """
    """
    liste = requete('/get_friend_list/',{'user_id':user_id})
    contenu = json.loads(liste.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True, contenu['status'] , contenu['friend_list']
    else:
        return False, contenu['status']

############################################
#                                          #     
#           Gestion des messages           #
#                                          #
############################################

def envoyer_message(user_id,group_id,message):
    """
    """
    envoi = requete('/add_message/',{'user_id' : user_id, 'group_id': group_id, 'message':message})
    contenu = json.loads(envoi.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True, contenu['status']
    else:
        return False, contenu['status']

def suprimer_message(message_id):
    """
    """
    supression = requete('/del_message/',{'message_id': message_id})
    contenu = json.loads(supression.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True, contenu['status']
    else:
        return False, contenu['status']

def charger_message(group_id):
    """
    """
    liste = requete('/get_message_list/',{'group_id': group_id})
    contenu = json.loads(liste.content.decode('utf-8'))
    if contenu['status'] == 'ok':
        return True, contenu['status'] , contenu['message_list']
    else:
        return False, contenu['status']