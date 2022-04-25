import curses
from fonctions import *
from time import sleep
from os import system
from multiprocessing import Process

status_connexion = False
dico_amis = {}
dico_groupes = {} 
user_id = 0
pseudo = 'wesh'
maxx = 0
maxy = 0


def clear():
	system('clear')

def screen_init(stdscr):
	stdscr.clear()
	stdscr.timeout(500)
	ecran_att(stdscr)

def logo():
	print("Salutation! Bienvenue dans")
	print("██████╗░██╗░░░██╗░░░░░░░█████╗░░█████╗░██████╗░██████╗░")
	print("██╔══██╗╚██╗░██╔╝░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
	print("██████╔╝░╚████╔╝░█████╗██║░░╚═╝██║░░██║██████╔╝██║░░██║")
	print("██╔═══╝░░░╚██╔╝░░╚════╝██║░░██╗██║░░██║██╔══██╗██║░░██║")
	print("██║░░░░░░░░██║░░░░░░░░░╚█████╔╝╚█████╔╝██║░░██║██████╔╝")
	print("╚═╝░░░░░░░░╚═╝░░░░░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░")
	print("pre-alpha")

def menu_principal():
	clear()
	logo()
	print("""
	Que voulez vous faire?
	1 : connexion
	2 : inscription
	q : quitter
		  """)
	reponse = input('choix [1][2][q] :')
	if reponse == '1':
		menu_connexion()
	elif reponse == '2':
		menu_inscription()
	elif reponse == 'q':
		clear()
		exit()
	else:
		clear()
		logo()
		print(reponse + " n'est pas un choix")
		menu_principal()

def menu_connexion():
	global status_connexion , user_id ,pseudo
	clear()
	logo()
	print(' ')
	pseudo = input("pseudo : ")
	mot_de_passe= input('mot de passe : ')
	print("connexion")
	# debug car flemme wola
	if pseudo == 'debug' and mot_de_passe == 'admin123':
		user_id = 123456789
		status_connexion = True
		print('compte debug')
		print('bienvenue ' + pseudo )
		sleep(2)
		main()
	status = connexion(pseudo,mot_de_passe)
	if status[0]:
		status_connexion = True
		main()
	else:
		print(status[1])
		input("entrée pour continuer")
		menu_principal()
	
def ecran_att(stdscr):
	maxy, maxx = stdscr.getmaxyx()
	bottomBox = curses.newwin(0,maxx-2,0,0)
	bottomBox.box()
	massage = 'bienvenue ' + str(pseudo)
	bottomBox.addstr(maxy//2,maxx//2-(len(massage)//2),massage)
#	bottomBox.addstr(maxy//2,maxx//2,massage)
	bottomBox.refresh()
	stdscr.refresh()
	#charge les amis
	#charge les groupe
	#charge les message
	while True:
		event = stdscr.getch()
		if event == ord("q"):
			break

def menu_inscription():
	clear()
	logo()
	print(' ')
	print(" attention, nous n'avons aucun moyen de recuperer un compte")
	pseudo = input("pseudo : ")
	mot_de_passe= input('mot de passe : ')
	mot_de_passe_confirmation= input('confirmer le mot de passe : ')
	status = inscription(pseudo,mot_de_passe,mot_de_passe_confirmation)
	if status[0]:
		print("compte crée")
		input("entrée pour continuer")
		menu_principal()
	else:
		print(status[1])
		input("entrée pour continuer")
		menu_principal()

def main():
	while status_connexion:
		curses.wrapper(screen_init)	# a meubler lol		
	else:
		menu_principal()
		
def hang():
	while True:
		temp = 1 + 1

if __name__ == '__main__':
	main()

