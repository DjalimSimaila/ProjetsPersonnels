import npyscreen
from fonctions import *
import time
from os import system
import curses.ascii
import threading


class Thread_messages(threading.Thread):
    def __init__(self, messages ,nom = '',):
        threading.Thread.__init__(self)
        self.nom = nom
        self.Messages = messages
        self.Terminated = False
    
    def run(self):
        update = 0
        while not self.Terminated:
            status = charger_message(self.Messages.group_id)
            if status[0] == False:
                return
            message_list = status[2]
            if len(message_list) > update:
                update = len(message_list)
                self.Messages.values = []
                for i in message_list:
                    message = ''
                    message = str(i[1]) +' '+ str(i[3])
                    self.Messages.values.append(message)
                    self.Messages.values.append(str(i[2]))
                    self.Messages.values.append("")
                    self.Messages.display()
            time.sleep(1)
    def stop(self):
        self.Terminated = True

class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.pseudo = ''
        self.user_id = 0
        self.list_ami = []
        self.list_group = []
        self.logo ="""
██████╗░██╗░░░██╗░░░░░░░█████╗░░█████╗░██████╗░██████╗░
██╔══██╗╚██╗░██╔╝░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝░╚████╔╝░█████╗██║░░╚═╝██║░░██║██████╔╝██║░░██║
██╔═══╝░░░╚██╔╝░░╚════╝██║░░██╗██║░░██║██╔══██╗██║░░██║
██║░░░░░░░░██║░░░░░░░░░╚█████╔╝╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
        """
        self.addForm('POST_CO', Menu_principal, name='PY-CORD')
        self.addForm('SIGNUP',Menu_Inscription, name = 'PY-CORD')
        self.addForm('LOGIN', Menu_Connexion, name='PY-CORD')
        self.addForm('MAIN', Menu_accueil, name='PY-CORD')

    def change_form(self, name):
        self.switchForm(name)
        self.resetHistory()

class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

"""
class NewMultiLineClass(npyscreen.MultiLine):
    def __init__(self):
        super(MultiLineEdit, self).__init__(screen, **keywords)
        self.group_index = None
        self.group_id = []
"""

class GroupeBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLine

class MessageBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLine

class Menu_principal(npyscreen.FormBaseNewWithMenus):

    def create(self):
        """
        liste_ami =  ['neo','Segpa'] // liste a afficher
        liste_ami.id_list =  [None,7] // liste des id de groupe
        liste_ami.group_index = None // l'index du group actuel
        message.group_id // id du groupe actuel
        """

        self.commandes = {
            '/help' : self.print_help,
            '/ajouter_ami' : self.add_to_friend,
            '/creer_groupe' : self.new_group,
            '/ajouter_dans_groupe' : self.add_to_group,
            '/suprimer_du_groupe' : self.remove_from_group,
            '/changer_groupe' : self.change_current_grp_cmd,
            }

        y , x = self.useable_space()
        
############################################
#                                          #     
#           Creation des widgets              #
#                                          #
############################################
        # old self.profil = self.add(npyscreen.BoxTitle, name='profil',rely= 2,relx= 2, max_width = (x//4), max_height = (y//4) - 2  )
        # old self.liste_ami= self.add(GroupeBox, name = 'amis/groupe',rely= y - (y//4*3),max_width = x//4)
    
    
        self.boite_texte = self.add(InputBox, name = "Partagez votre savoir",rely= y - (y//8) ,relx= x - (x//4 * 3) -14 )
        self.Messages = self.add(MessageBox, name='grp',rely= 2,relx= x - (x//4 * 3) - 14 ,max_width = x//4 * 3 - 9, max_height = y - (y//8) - 2 )
        
        self.liste_ami= self.add(GroupeBox, name = 'amis/groupe',rely= 2,relx= 2,max_width = x//4 - 15)
        self.liste_user = self.add(GroupeBox ,rely= 2,relx= x - x//10,  max_height = y - (y//8) - 2)
        
        self.liste_ami.group_index = None
        self.Messages.group_id = None
        self.thread = ""
        #
        #self.liste_ami.handlers.update({27:self.change_current_grp})
        self.liste_ami.handlers.update({curses.ascii.NL :self.test }) # curses.ascii.NL means the New Line key (Enter)
        self.liste_ami.add_handlers({"^H" :self.change_current_grp })
        self.boite_texte.add_handlers({"^S" :self.send_message })

############################################
#                                          #     
#             Gestion des menu             #
#                                          #
############################################

        self.m1 = self.add_menu(name='Menu utilisateur',shortcut='^M')
        self.m1.addItemsFromList([
            ('Deconnection',self.change_to_main,"d",),
            ('DEBUG',self.debug,'Q'),
            ('Aide',self.print_help,'Q'),
            ('Fermer ce menu',self.change_to_post_co,"f")
        ])
        self.m4 = self.m1.addNewSubmenu(name='supprimer un ami')


        self.m2 = self.add_menu(name='Menu groupe',shortcut='^G')
        self.m2.addItemsFromList([
            ('retirer un ami dans le groupe',self.change_to_post_co,'g'),
            ('Suprimer le groupe',self.change_to_post_co,"f")
        ])
        self.m3 = self.m2.addNewSubmenu(name='Ajouter un ami dans le groupe')

############################################
#                                          #     
#             Gestion des amis             #
#                                          #
############################################
        
    def update_menu_amis(self):
        liste_ajout_ami_grp = []
        liste_retait_ami = []
        for i in range(len(self.liste_ami.values)):
            if self.liste_ami.id_list[i] == None:
                liste_ajout_ami_grp.append((self.liste_ami.values[i], self.add_to_group, None ,None,(str(self.liste_ami.values[i]),)))
                liste_retait_ami.append((self.liste_ami.values[i], self.remove_from_friend, None ,None,(str(self.liste_ami.values[i]),)))
        self.m3.addItemsFromList(liste_ajout_ami_grp)
        self.m4.addItemsFromList(liste_retait_ami)

    def update_liste_amis(self):
        self.liste_ami.id_list = []
        self.liste_ami.group_index = None
        self.liste_ami.values = []    
        amis = charger_amis(self.parentApp.user_id)
        if amis[0]== True: 
            for i in amis[2]:
                self.liste_ami.values.append(i)
                self.liste_ami.id_list.append(None)
        groupes = charger_groupe(self.parentApp.user_id)
        if groupes[0] == True: 
            for i in groupes[2]:
                self.liste_ami.values.append(i[0])
                self.liste_ami.id_list.append(i[1])
        self.update_menu_amis()
        
    def add_to_friend(self,pseudo_ami):
        status = ajouter_amis(self.parentApp.pseudo,pseudo_ami)
        if status[0] == True:
            npyscreen.notify_confirm(pseudo_ami + ' a été ajouté a vos amis')
            self.update_liste_amis()
        else:
            npyscreen.notify_confirm(status[1])

    def remove_from_friend(self,pseudo_ami):
        status = retirer_amis(self.parentApp.pseudo,pseudo_ami)
        if status[0] == True:
            npyscreen.notify_confirm(pseudo_ami + ' a été retiré de vos amis')
            self.update_liste_amis()
        else:
            npyscreen.notify_confirm(status[1])

############################################
#                                          #     
#           Gestion des groupes            #
#                                          #
############################################

    def change_current_grp_cmd(self,grp_name):
        if grp_name in self.liste_ami.values:
            valeur = self.liste_ami.values.index(grp_name)
            if self.liste_ami.group_index != valeur :
                self.liste_ami.group_index = valeur
                self.Messages.name =  self.liste_ami.values[self.liste_ami.group_index]
                self.Messages.group_id = self.liste_ami.id_list[self.liste_ami.group_index]
                if self.Messages.group_id != None: self.load_messages()
                self.Messages.display()
        else:npyscreen.notify_confirm('Groupe introuvable')            
    
    def change_current_grp(self,wut):
        if self.liste_ami.group_index != self.liste_ami.value :
            self.liste_ami.group_index = self.liste_ami.value
            self.Messages.name =  self.liste_ami.values[self.liste_ami.group_index]
            self.Messages.group_id = self.liste_ami.id_list[self.liste_ami.group_index]
            if self.Messages.group_id != None: self.load_messages()
            self.Messages.display()

    def new_group(self,nom_grp):
        status = ajouter_dans_groupe(self.parentApp.pseudo,nom_grp)
        if status[0] == True:
            npyscreen.notify_confirm('Le groupe a été crée')
            self.update_liste_amis()
        else:
            npyscreen.notify_confirm(status[1])
    
    def remove_from_group(self,pseudo):
        if self.Messages.group_id != None:
            status = retirer_dans_groupe(pseudo,self.Messages.name)
            npyscreen.notify_confirm(str(status[1]))
        else:
            npyscreen.notify_confirm("Selectionnez un groupe avant de performer cet operation")

    def add_to_group(self, pseudo_ami):
        if self.Messages.group_id != None:
            status = ajouter_dans_groupe(pseudo_ami,self.Messages.name)
            npyscreen.notify_confirm(str(status[1]))
        else:
            npyscreen.notify_confirm("Selectionnez un groupe avant de performer cet operation")

    def debug(self):
        npyscreen.notify_confirm([
            str(len(self.liste_ami.values)),
            str(self.liste_ami.values),
            str(self.liste_ami.id_list),
            str(self.parentApp.pseudo),
            str(self.Messages.group_id)
            ])
    
    def test(self,wut):
        npyscreen.notify_confirm('boo')
    
############################################
#                                          #     
#           Gestion des messages           #
#                                          #
############################################

    def send_message(self,wut):
        if self.boite_texte.value[0] == '/':
            commande = self.boite_texte.value.split()
            if len(commande) > 1:
                args = ''
                for i in commande:
                    if '/' in i:pass
                    else:
                        args += i
                try:
                    self.commandes[commande[0]](args)
                    self.boite_texte.value = ''
                except:
                    npyscreen.notify_confirm('commande inexistante')
            else:
                try:
                    self.commandes[commande[0]]()
                    self.boite_texte.value = ''
                except:
                    npyscreen.notify_confirm('commande inexistante')
        else:
            if self.thread != '':
                self.thread.stop()
            if self.Messages.group_id != None:
                message = self.boite_texte.value
                envoyer_message(self.parentApp.user_id,self.Messages.group_id,str(message))
                self.boite_texte.value = ''
                self.load_messages()
            else:
                pass

    def load_messages_old(self):
        status = charger_message(self.Messages.group_id)
        if status[0] == False:
            return
        message_list = status[2]
        self.Messages.values = []
        for i in message_list:
            message = ''
            message = str(i[1]) +' '+ str(i[3])
            self.Messages.values.append(message)
            self.Messages.values.append(str(i[2]))
            self.Messages.values.append("")
            self.change_to_post_co()

    def load_messages(self):
        self.thread = Thread_messages(self.Messages)
        self.thread.start()

######################################################
    def print_help(self):
        npyscreen.notify_confirm([
            "A cause d'un soucis au niveau de la bibliotheque, pour charger les messages du groupe selectioné veuillez appuyer sur ctrl + g et pour envoyer un message ctrl + s",
            "",
            "",
            "Commandes",
            "/help : affiche cette pop up",
            "/ajouter_ami [pseudo] : ajoute un utilisateur dans la liste d'amis",
            "/creer_groupe [nom du groupe] : Crée un groupe",
            '/changer_groupe [nom du groupe] : change le groupe actuel',
            "/ajouter_dans_groupe [pseudo] : ajoute un utilisateur dans le groupe",
            "/suprimer_du_groupe [pseudo] : supprime un utilisateur du groupe",
        ],'Aide',wrap = True,)
                                     
    def change_to_main(self):
        self.Messages.values = []
        self.Messages.name = 'groupe'
        self.parentApp.change_form('MAIN')

    def change_to_post_co(self):
        self.parentApp.change_form('POST_CO')
########################################################
class Menu_accueil(npyscreen.FormBaseNew):

    def create(self):
        y , x = self.useable_space()
        self.add(InputBox, editable = False,value= self.parentApp.logo, max_width = 60,max_height=10, relx=(x//2) - 60 //2 )
        self.add(npyscreen.ButtonPress, name="Connection", when_pressed_function=self.to_login,relx=(x//2) - 10 //2, rely= y//2 - 2)
        self.add(npyscreen.ButtonPress, name="Inscription", when_pressed_function=self.to_signup,relx=(x//2) - 10 //2, rely= y//2 )
        self.add(npyscreen.ButtonPress, name="Quitter", when_pressed_function=self.exit_application,relx=(x//2) - 10 //2, rely= y//2 + 2)

    def to_login(self):
        self.parentApp.change_form('LOGIN')

    def to_signup(self):
        self.parentApp.change_form('SIGNUP')

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

class Menu_Connexion(npyscreen.ActionForm):

    def create(self):
        y , x = self.useable_space()
        self.add(InputBox, editable = False,    value = self.parentApp.logo, max_width = 60,max_height=10, relx=(x//2) - 60 //2 )
        self.pseudo = self.add(npyscreen.TitleText, name='Pseudo:',relx=(x//3) - 10 //2, rely= y//2 - 2)
        self.mot_de_passe = self.add(npyscreen.TitlePassword, name='Mot de passe:',relx=(x//3) - 10 //2, rely= y//2)
        
    def on_ok(self):
        etat = connexion(self.pseudo.value,self.mot_de_passe.value)
        if etat[0] == True:
            self.parentApp.pseudo = self.pseudo.value
            self.parentApp.user_id = etat[2]
            
            self.parentApp._Forms['POST_CO'].update_liste_amis()
            
            npyscreen.notify_confirm('bienvenue '+ self.pseudo.value + '\n' + ' Entrée pour continuer')
            self.parentApp.change_form('POST_CO')
        else:
            npyscreen.notify_confirm(etat[1])
            self.pseudo.value = ''
            self.mot_de_passe.value = ''
            self.parentApp.change_form('LOGIN')
    
    def on_cancel(self):
        self.parentApp.change_form('MAIN')
    

class Menu_Inscription(npyscreen.ActionForm):

    def create(self):
        y , x = self.useable_space()
        self.add(InputBox, editable = False,    value = self.parentApp.logo, max_width = 60,max_height=10, relx=(x//2) - 60 //2 )
        self.pseudo = self.add(npyscreen.TitleText, name='Pseudo:',relx=(x//3), rely= y//2 - 2)
        self.mot_de_passe = self.add(npyscreen.TitlePassword, name='Mot de passe:',relx=(x//3), rely= y//2)
        self.mot_de_passe_conf = self.add(npyscreen.TitlePassword, name='Confirmez le mdp:',relx=(x//3) - 10 //2, rely= y//2 + 2)
    
    def on_ok(self):
        etat = inscription(self.pseudo.value,self.mot_de_passe.value,self.mot_de_passe_conf.value)
        if etat[0] == True:
            npyscreen.notify_confirm('compte crée' + '\n' + ' Entrée pour continuer')
        else:
            npyscreen.notify_confirm(etat[1])
            self.pseudo.value = ''
            self.mot_de_passe.value = ''
            self.mot_de_passe_conf.value = ''

    def on_cancel(self):
        self.parentApp.change_form('MAIN')


if __name__ == '__main__':
    TestApp = MyApplication().run()