import fonctions
from flask import Flask, request, render_template, jsonify, json
app = Flask(__name__)



@app.route('/lol/', methods=['GET'])
def index():
    return render_template('inscription.html')

@app.route('/lol/', methods=['POST'])
def lol():
    pseudo , mdp = request.form['pseudo'], request.form['mot_de_passe']
    return {"status":"fait",'test':'jessss'} , 200


@app.route('/test/', methods=['POST','GET'])
def test():
    print("je suis le test")
    return {"test": "yoloooooo"} # response to your request.

############################################
#                                          #
#           Connexion/Inscription          #
#                                          #
############################################
#
# connexion : fait
#
# inscription : fait

@app.route('/connexion/', methods=['GET'])
def connexion_GUI():
    return render_template('connexion.html')

@app.route('/connexion/', methods=['POST'])
def connexion():
    # les donnees recu par cette fonction doit etre sous la forme {"pseudo": "User",'mot_de_passe': 'GFSDSDSQDF'}
    pseudo, mot_de_passe_hash  = request.form['pseudo'] , request.form['mot_de_passe']
    print(pseudo,mot_de_passe_hash)
    return fonctions.connexion(pseudo,mot_de_passe_hash)


@app.route('/add_user/', methods=['GET'])
def add_user_GUI():
    return render_template('inscription.html')

@app.route('/add_user/', methods=['POST'])
def add_user():
    # les donnees recu par cette fonction doit etre sous la forme {"pseudo": "User",'mot_de_passe': 'GFSDSDSQDF'}
    
    pseudo, mot_de_passe_hash  = request.form['pseudo'] , request.form['mot_de_passe']
    print(pseudo, mot_de_passe_hash)
    return fonctions.add_user(pseudo,mot_de_passe_hash)


############################################
#                                          #     
#             Gestion des amis             #
#                                          #
############################################
#
# ajouter ami : fait
#
# retirer ami :  fait
#
# lister les amis : fait

@app.route('/add_to_friends/', methods=['POST'])
def add_to_friend():
    # les données recu par cette fonction doit etre sous la forme {"pseudo" : "User", "pseudo_ami" : User2}
    pseudo, pseudo_ami = request.form['pseudo'], request.form['pseudo_ami']
    return fonctions.add_friends(pseudo,pseudo_ami)

@app.route('/del_from_friend/', methods=['POST'])
def del_from_friend():
    # les données recu par cette fonction doit etre sous la forme {"pseudo" : User, "pseudo_ami" : User2 }
    pseudo, pseudo_ami = request.form['pseudo'], request.form['pseudo_ami']
    return fonctions.delete_friend(pseudo,pseudo_ami)

@app.route('/get_friend_list/', methods=['POST'])
def get_friend_list():
    # les données recu par cette fonction doit etre sous la forme {"user_id" : "123"}
    user_id = request.form['user_id']
    return fonctions.list_friends(user_id)


############################################
#                                          #     
#           Gestion des groupes            #
#                                          #
############################################
#
# ajouter un utilisateur dans groupe : fait
#
# retirer un utilisateur dans groupe : fait
#
# lister groupes : fait


@app.route('/add_to_group/', methods=['POST'])
def add_to_group():
    # les données recu par cette fonction doit etre sous la forme {"pseudo" : "User",'group_name': 'les amis'}
    pseudo, group_name = request.form['pseudo'], request.form['group_name']
    return fonctions.add_user_in_group(pseudo,group_name)

@app.route('/del_from_group/', methods=['POST'])
def del_from_group():
    # les données recu par cette fonction doit etre sous la forme {"pseudo" : "User",'group_name': 'les amis'}
    pseudo, group_name = request.form['pseudo'], request.form['group_name']
    return fonctions.delete_user_in_group(pseudo,group_name)

@app.route('/get_group_list/', methods=['POST'])
def list_group():
    # les données recu par cette fonction doit etre sous la forme {"user_id" : "123"}
    user_id = request.form['user_id']
    return fonctions.list_usr_groups(user_id)

@app.route('/get_group_user_list/', methods=['POST'])
def list_user_group():
    # les données recu par cette fonction doit etre sous la forme {"group_id" : "123"}
    group_id = request.form['group_id']
    return fonctions.list_usr_on_group(int(group_id))
 
############################################
#                                          #     
#           Gestion des messages           #
#                                          #
############################################
#
# Envoyer un message : fait
#
# Suprimer un message : fait
#
# lister les messages : fait

@app.route('/add_message/', methods=['POST'])
def add_message():
    # les données recu par cette fonction doit etre sous la forme {"user_id" : "123",'grp_id','message': 'Salut'}
    user_id, group_id, message = request.form['user_id'], request.form['group_id'], request.form['message']
    return fonctions.add_message_in_group(message,user_id,group_id)

@app.route('/del_message/', methods=['POST'])
def del_message():
    # les données recu par cette fonction doit etre sous la forme {"message_id" : "123"}
    mess_id = request.form['message_id']
    return fonctions.delete_message(mess_id)

@app.route('/get_message_list/', methods=['POST'])
def get_message():
    # les données recu par cette fonction doit etre sous la forme {"message_id" : "123"}
    group_id = request.form['group_id']
    return fonctions.list_message(group_id)

############################################
#                                          #     
#           Gestion utilisateur            #
#                                          #
############################################
#
# changer de pseudo : fait
#
# changer de mot de passe : fait

@app.route('/change_psswd/', methods=['POST'])
def change_passwd():
    # les donnees recu par cette fonction doit etre sous la forme {"user_id": "123",'mot_de_passe': 'GFSDSDSQDF'}
    user_id, nouveau_mot_de_passe = request.form['user_id'], request.form['mot_de_passe']
    return fonctions.changer_mdp(user_id, nouveau_mot_de_passe)

@app.route('/change_pseudo/', methods=['POST'])
def change_pseudo():
    # les donnees recu par cette fonction doit etre sous la forme {"user_id": "123","pseudo": "User"}
    user_id, nouveau_pseudo = request.form['user_id'], request.form['pseudo']
    return fonctions.changer_pseudo(user_id, nouveau_pseudo)


@app.route('/A/', methods=['GET'])
def AAAAAAAAAAAAA():
    return render_template('connexion.html')

"""
@app.route('/postco/', methods=['GET'])
def post_co():
    return render_template('index.html
    """



if __name__ == "__main__":
    app.run(host="localhost", port = 5016,debug=True, ssl_context='adhoc')
