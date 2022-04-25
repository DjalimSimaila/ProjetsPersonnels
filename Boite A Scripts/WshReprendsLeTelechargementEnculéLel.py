#Auteur : Djalim Simaila <Djalim.S@outlook.fr>


# %%
#--------------- Memo -------------------

#http://mafreebox.freebox.fr/api/v6/
#json.dumps(variables).encode('utf-8')
#json.loads(variable.decode('utf-8'))

"""
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
"""

"""
content_post_login_authorise = json.dumps(login).encode('utf-8')
post_login_authorise = requests.post(base_url+"login/authorize/", content_post_login_authorise)
print(post_login_authorise.status_code)
content_post_login_authorise = post_login_authorise.content
content_post_login_authorise = json.loads(content_post_login_authorise.decode('utf-8'))
"""
# %%
import hmac
import requests
import json
import hashlib
import base64
import argparse
from os import system, name 
from time import sleep
# %%
#--------------Fonctions-----------------
def api_get(call:str, *headers: dict)-> dict:
   """
   Donc basiquement c'est une fonction qui fait un GET, tu deffinit l'url de base/racine dans une variable globale "base_url"
   et tu passe en parametre l'appel de l'api, tu peut metre en bonus des headers 

   :param call: l'appel de l'api
   :type call: str , chaine de charactere
   :param headers: l'entete de l'http
   :type headers: dict, dictionnaire
   :return: la reponce de l'api
   :r type: dict, dictionnaire
   """
   global base_url
   if len(headers) > 0:
      get_call = requests.get(base_url+call, headers=headers)
   else:
      get_call = requests.get(base_url+call)
   print("GET " + call)
   if get_call.status_code != 200:
      error_get_call = get_call.content
      error_get_call = json.loads(error_get_call.decode('utf-8'))
      msg = error_get_call["msg"]
      error_code = error_get_call["error_code"]
      raise Exception("Salam mec, t'as fait un GET c'est cool mais j'ai recu l'erreur {}, la freebox me dit ;'{}' et aussi '{}'".format(get_call.status_code,msg,error_code))
   content_get_call = get_call.content
   content_get_call = json.loads(content_get_call.decode('utf-8'))
   if "success" in content_get_call.keys():
      if content_get_call["success"] == False:
         raise Exception("Bonjour 'inserer terme inclusif ici', t'as fait un get, t'as eu un status code 200 mais le succes est false, chelou nan?" )
      return content_get_call["result"]
   else:
      return content_get_call     

def api_post(data: dict ,call : str, *headers : dict)-> dict:
   """
   Donc basiquement c'est une fonction qui fait un POST, tu deffinit l'url de base/racine dans une variable globale "base_url"
   et tu passe en parametre l'appel de l'api, les données que tu envois et tu peux metre en bonus des headers

   :param data: Les données que tu veux envoyer
   :type data: dict, dictionnaire
   :param call: l'appel de l'api
   :type call: str , chaine de charactere
   :param headers: l'entete de l'http
   :type headers: dict, dictionnaire
   :return: la reponce de l'api
   :r type: dict, dictionnaire
   """
   global base_url
   data = json.dumps(data).encode('utf-8')
   if len(headers) > 0 :
      post_call = requests.post(base_url+call, data=data, headers=headers)
   else:
      base_url = base_url
      call = call
      post_call = requests.post(base_url+call, data=data)
   print("POST " + call)
   if post_call.status_code != 200:
      error_post_call = post_call.content
      error_post_call = json.loads(error_post_call.decode('utf-8'))
      msg = error_post_call["msg"]
      error_code = error_post_call["error_code"]
      raise Exception("Salam mec, t'as fait un POST c'est cool mais j'ai recu l'erreur {}, la freebox me dit ;'{}' et aussi '{}'".format(post_call.status_code,msg,error_code))
   content_post_call = post_call.content
   content_post_call = json.loads(content_post_call.decode('utf-8'))
   if "success" in content_post_call.keys():
      if content_post_call["success"] == False:
         raise Exception("Bonjour 'inserer terme inclusif ici', t'as fait un post, t'as eu un status code 200 mais le succes est false, chelou nan?" )
      return content_post_call["result"]
   else:
      return content_post_call 

def api_put(data, call,*headers):
   """
   """
   global base_url
   data = json.dumps(data).encode('utf-8')
   if len(headers) > 0 :
      put_call = requests.put(base_url+call, data=data, headers=headers)
   else:
      base_url = base_url
      call = call
      put_call = requests.put(base_url+call, data=data)
   print("PUT " + call)
   if put_call.status_code != 200:
      error_put_call = put_call.content
      error_put_call = json.loads(error_put_call.decode('utf-8'))
      msg = error_put_call["msg"]
      error_code = error_put_call["error_code"]
      raise Exception("Salam mec, t'as fait un PUT c'est cool mais j'ai recu l'erreur {}, la freebox me dit ;'{}' et aussi '{}'".format(put_call.status_code,msg,error_code))
   content_put_call = put_call.content
   content_put_call = json.loads(content_put_call.decode('utf-8'))
   if "success" in content_put_call.keys():
      if content_put_call["success"] == False:
         raise Exception("Bonjour 'inserer terme inclusif ici', t'as fait un put, t'as eu un status code 200 mais le succes est false, chelou nan?" )
      return content_put_call["result"]
   else:
      return content_put_call 

def generer_mot_de_passe(message:str, key:str)-> str:
   key = bytes(key, 'latin-1')
   message = bytes(message, 'latin-1')
   password = hmac.new(message,key,hashlib.sha1).hexdigest()
   #return str(password)
   return password

def autorise_moi_la_con_de_tes_morts(app_id,app_name,app_version,device_name):
   """
   Je trouve que le nom de la fontion est assez descrptif mais je dois tout de meme respecter les regles et tout et tout
   donc oui tu donne un app_id name version et nom de peripherique et cette fonction se charge de te donner une session valide
   va tout de meme falloir que tu accepte sur la freebox mais voila voila

   :param app_id: un identifiant pour le script
   :param app_name: un nom pour le script
   :param app_version: une versios pour le script
   :param device_name: le doux nom de l'appareil d'ou va tourner le script
   :return: le session token a foutre dans chacun de tes appels
   :r type: jsp encore je dois faire un test sur terrain,
   """
   
   login = {
      "app_id": app_id,
      "app_name": app_name,
      "app_version": app_version,
      "device_name": device_name
   }
   status_list = {
   "unknown" : "yo t'as un probleme avec l'app token soit il existe pas, soit il est vieux as fuck",
   "pending" :	"hello va falloir que tu m'authorise, check ta freebox",
   "timeout" : "bichiour il semblerais que tu n'a pas ete asser rapide j'ai timeout",
   "granted" : "authorisé bg bienvenue dans la team",
   "denied"  : "La freebox a decidé de ton sort et sa sentence est irrevocable (oui tu as ete refusé bg)"
   }

   try:
      login = api_post(login,"/login/authorize/")
   except:
      raise Exception("t'es sur qu'il y a une freebox a cet ip ou se reseau?")
   track_id = login["track_id"]
   status = "pending"

   while status == "pending":
      content_status = api_get("/login/authorize/"+str(track_id))
      status = content_status["status"]
      # Fix : a simplifier ,c'est moche et degueu wola
      if status != "pending" :
         if status == "granted":
            pass
         else : 
            raise Exception(status_list[status])

   app_token = login["app_token"]
   challenge = content_status["challenge"]
   mot_de_passe = generer_mot_de_passe(app_token,challenge)
   data = {
      "app_id": app_id,
      "app_verison": app_version,
      "password": mot_de_passe
   }
   session = api_post(data,"/login/session")
   session_token = session['session_token']
   return session_token

def ckelversion():
   """
   Cette fontion permet de generer la base url avec la version la plus recente de l'api freebox
   """
   global base_url
   api_version = api_get("/api_version")['api_version']
   api_version = api_version[0]
   base_url = base_url + "/api/v" + str(api_version)
   print(base_url)
   return

def clear(): 
   """
   Petite fonction volée sur internet qui permet de clear le screen
   """
   # for windows 
   if name == 'nt': 
     _ = system('cls') 
  
   # for mac and linux(here, os.name is 'posix') 
   else: 
      _ = system('clear') 
   return

def check_argument():
   print("""
   Utilisation : wsh reprends le telechargment enculé .py [OPTION]

   --help, -H                          affiche cette page help

   --mode [1|2|3], -M [1|2|3]          definit le mode que le scrpit va effectuer
                                       1 : verifie periodiquement l'etat du wifi et le desactive si activé
                                       2 : ralenti la vitesse de connection d'une ip sur le reseau
                                       3 : verifie peridiquement l'etat d'un telechargement et le reactive si desactivé

   --ip                                precise l'adresse ipv4 de l'appareil a ralentir
                                       (uniquement quand --mode 2 est en argument)

   --dl_id                             precise l'identifiant du telechargement
                                       (uniquement quand --mode 3 est en argument)
   """)

# %%
#####################################################################################

# vref c'est ici que tu commence a poser ta merde

"""
commence par poser l'ip de la freebox bg
exemple:
   base_url= "192.168.1.69
"""
base_url= "http://192.168.1.69"
####################################################################################
"""

"ensuite ici tu met les info relatif au script"

exemple:
   app_id = "app_test"
   app_name = "application teste"
   app_version = "0.0.0"
   device_name = "ordinateur de Djalim le grand bg"
"""

app_id = "test_auto_redownloader"
app_name = "re-down"
app_version = "0.0.1"
device_name = "Djalim tu crois que c'est qui"
####################################################################################
if __name__ == "__main__":

   # Authentification
   print("salam mec je check l'ip de la freebox , je me connecte et je suis a toi .w.")
   try:
      ckelversion()
   except:
      raise Exception(" OI CUNT, ya pas de freebox sur le reseau ou l'ip est fausse jsp moi")
   session_token = autorise_moi_la_con_de_tes_morts(app_id,app_name,app_version,device_name)
   auth = {"XFbx-App-Auth": session_token}
   #print(type(auth))
   #auth_test = api_get("/login/session", auth)
   clear()


   # %%
   print("""
   Bienvenue dans un script assez chiant mais qui te donne full power sur ta freebox car tu sait programmer

   alors tu veux faire quoi?
      [1]      Je veux que le wifi reste desactivé a jamais
      [2]      Je veux ralentir la co de quelqu'un
      [3]      Je veux que ce putain de telechargment arrete de s'arreté
      [quit]   Je veux me tirer d'ici
   """)
   choix = str(input("[1]/[2]/[3]/[quit] :"))

   #POURQUOI YA PAS DE SWITCH/CASE SUR PYTHON C'EST QUOI CETTE ARNAQUE WSH JE SUIS OUTRÉ

   #[1]
   def wsh_le_wifi_casse_toi(nb_de_minute: int):
      """
      Cette fonction fait en sorte que le wifi reste desactiver et que dans le cas ou un petit malin reactive le wifi
      celui ci soit redeactivé a nouveau
      il se deactive apres le nombre de seconde donné en parametre, si aucun nombre n'es specifié il prendra 60 min
      par defaut
      """
      
      while nb_de_minute > 0:
         etat = api_get("wifi/config")
         if etat["enabled"] == True:
            api_put({"enabled":False},"/wifi/config/")
            print("le wifi a ete deactivé mon gars profite de la bande passante .w.")
            sleep(60)
            nb_de_minute -= 1
         else:
            sleep(60)
            nb_de_minute -= 1
      print("le nombre de minute a été atteint, reactivation du wifi")
      api_put({"enabled":True},"/wifi/config/")
      return

   #[2]
   def toi_tu_me_fais_clairement_chier():
      """

      """

   #[3]
   def continue_de_telecharger():
      """
      """

      dl_liste = api_get("/downloads/")
      for id in dl_liste:
         print(id, " - " ,dl_liste["name"])
      choix = str(input("saisis l'id du telechargement :"))
      dl = api_get('/download/'+ choix )
      print("ok ok je go l'empecher de dormir ce batar laisse moi en background et vit ta vie")
      while dl["status"] != "done" or "seeding" :
         
         if dl["status"] == "queued" or "downloading" :
            sleep(60)

         if dl["status"] == "error" or "stopped" :
            api_put({"status":"retry"},"/download/"+choix)
            print("telechargment réactivé")
            sleep(60)
         dl = api_get('/download/'+ choix )


   # %%
