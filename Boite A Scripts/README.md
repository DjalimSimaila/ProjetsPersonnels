## Economie.py

Ce script permet de desactiver des core et la carte graphique nvidia dans un pc 
portable
Pour eteindre les core ce script envoie 0 au fichier correspondant a chaque core
pour le cas du GPU, ce script utilise des appels ACPI qui eteint directement 
le materiel, a noter que le systeme d'exploitation ne detecte pas le changement et
que donc il peu falloir unload les module li{}es a la carte graphique

## EstCeQueJePasseLeSemestreV2.py

Ce script permet de calculer les differentes moyenne li{}e a chaque matiere du
BUT informatique et indique si , selon les notes, le semestre est valid{}e ou pas
La version 2 correspond au modifications faites pour supporter le 2e semestre

## HistStats.py

Petit script ecris en 5 minutes pour me distraire d'un cours tres peu pationnant.
Ce script lit le fichier .zsh_history et retoune les commandes et leur nombre 
d'utilisation dans l'ordre decroissant

## MangaScanner.py

Script qui via l'intermediare de Tesseract-osr, lit un dossier contenant un manga
sous formes et compile l'integralit{} du texte contenu dans ces images. Le texte est 
ensuite filtr{} en fonction de si il contient la chaine de caractere demmand{}e
Le script retourne apres dans un fichier la liste des fichier contenant la chaine
de caractere.
Ce script m'a permit de retrouver une citation dans un de mes manga prefer{}e sans
avoir a relire l'integralit{} de l'oeuvre

## MangaToPdf

Script qui compile l'integralit{} d'un manga contenu dans un dossier 
( sous l'aborecensce "manga/chapitre/page.jpeg") sous forme de pdf chaqu'un 
contenant un chapitre

## TournoisEnding

Petit script qui automatique la gestion d'un tournoi quelconque

## VoleurDeManga.py

Parser du site sushi-scan.su, ce scipt permet de telecharger l'integralit{}
d'un manga present dans le site, j'utilise beautiful soup pour recuperer la page et
les lien vers les images contenu dans ces pages, une fois les lien direct recuper{}s
j'utilse simplement wget pour les telecharger

## WshReprendsLeTelechargmentEncul{}Lel.py

Script qui prends partie de l'api interne et tres bien document{} de la freebox
revolution qui permet de gerer les telechargment du client torrent interne de la 
freebox, notemment un telechargement qui n'arrete pas de ce suspendre pour aucune 
raison apparente

## YalmPerser.py

Simple prototype fonctionnel de parser yalm pour le projet de 1ere ann{}e de BUT info

