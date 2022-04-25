# Pycord

## Dependances

- Python3
- curses
- npyscreen

## Instalation

```
$ git glone https://framagit.org/terminale-nsi-2020-2021/groupe-3-cl-ment-djalim/votre-projet.git
```

## Uitlisation

### Lancer le serveur

 ```
$ cd serveur
$ python3 serveur.py 
```

### Clients

##### Console
```
$ cd client
$ python3 client.py 
```

##### HTML

https://serveur-pgdg.net:5016


## API
l'api complete et detaillé se trouve dans client/fonctions.py

# Cahier des Charges


notions et algos du cours:
- html / css / javascript
- Bases de donnes sql
- flask
- compression (huffman)

pas du cours

- algorithme de hashage pour les mdp
- algorithme de cryptage

Idée globale:

> Créer un logiciel de communication en message instantané qui permet d'envoyer des messages a des utilisateurs ou a un groupe de d'utilisateurs.


# 1ere partie, le backend
Gestion des comptes utilisateurs (pseudo + mots de passes), des groupes de chat, et des messages

## - gestion des compte et des groupes 

les groupes et les utilisateurs seront stoqués dans une base de données SQL


| utilisateurs | valeur |
|-|-|
| user_id | int |
| pseudo | str |
| mot_de_passe_hash | str |
| id_groupe | table|
| id_amis| table |


| groupes | valeur |
|-|-|
| grp_id | int |
| nom_du_groupe | str |
| user_id| str |

| lien usr grp | valeur |
|-|-|
| grp_id | int |
| user_id| str |

<font color='blue'>Peut être rajouter une table 'role' qui lie les utilisateurs et les groupes auquels ils on accès ?</font>

| lien amis | valeur |
|-|-|
| user_id| str |
| user_id| str |

![img](https://cdn.discordapp.com/attachments/561585323616763924/817820160345374760/20210306_190511.jpg)

## - gestion des messages

Le format qui stoque les messages se doit de pouvoir :
 
 - garder la date, l'heure et le contenu du message
 - etre modifiable pour genre supprimer des messages
 - etre cryptable 
 - etre compressable 
 
le format csv remplit ces conditions on aurais donc un fichier:

"id du groupe".csv

et les lignes ressembleraient a ceci:

|'id_user'|date/heure|message| 
 |-|-|-|
 |123456|00:00_2021/01/01|'salut'|
|987654|00:01_2021/01/01|'salut mon pote'|


## Gestion des fichiers sur le serveur

Il faudra stoquer les photo de profils, les messages, et les éventuels fichiers partagés par les utilisateurs.

<pre>
Serveur
├── Start-server.py
├── database.sql
├── groups-texts   ----------------->  # Ce dossier stoque les dossiers des differents groupes
│   ├── 00                            # Le dossier associé a un groupe porte son id comme nom
│   │   ├── 00.csv
│   │   ├── 00.csv.bak ----------->  # Copie de secours du fichier qui contiendra les messages
│   │   ├── 00.zip     ----------->  # Version compressée du fichier qui contiendra les messages
│   │   └── shared    ------------>  # Ce dossier contient les fichiérs partagés par le groupe (*)
│   │       ├── devoir_a_rendre.doc
│   │       └── mon_chat.png
│   └── 01
│       ├── 01.csv
│       ├── 01.csv.bak
│       ├── 01.zip
│       └── shared
│           └── photo_de_vacance.jpeg
└── profile_pictures  -------------> # Ce dossier contient toute les photos de profils
    ├── 123456.png   --------------> # Les photos de profils portent l'id de l'utilisateur en nom
    └── 987654.png
</pre>

(*) On imposera probablement un taille limite et/ou on les supprimerera apres une periode de temps donné.

# 2e Partie, le frontend
interface graphique + fonctionalités

##  Interface

une interface moderne type skype ou messenger

![img](https://cdn.discordapp.com/attachments/561585323616763924/817849654548496444/20210306_210123.png)


## fonctionalités du coté client

- permetre l'inscription et la connection

- faire en sortes qu'on puisse personnaliser (creer des groupes ...)

- télécharger et uploader les photo de profils

- télécharger et afficher que les dernier 50 messages ( on peut mettre ca dans le backend genre un script qui fait que le csv a tjr 50 lignes et les ancienne sont compressées et archivées

- faire les requettes pour afficher les utilisateurs qu'on a en amis et les groupes auquels on appartient

- algorithme de recherche des utilisateurs (peut etre pas necessaire du fait qu'on utilise sql)

- detecter les utilisateurs en ligne 

- pourvoir envoyer autre chose que du texte (image,son,video,doc ...), 

- faire des groupes vocaux 

