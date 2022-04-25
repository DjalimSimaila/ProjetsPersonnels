import random
import csv

def creer_calcul(difficulte:int )->str:
    """
    Cette fonction crée un calcul au hasard entre une addition, soustrction, multiplication et division euclidienne.
    Elle prend en compte la difficulté, choisie par l'utilisateur. 
    En difficulté facile (difficulté = 0), les - sont positives, les nombres sont des entiers positifs, les * et les / sont les tables de 1 à 10.
    En difficulté normale (difficulté = 1), les - peuvent être négatives, il y a des nombre entiers positifs et négatifs pour les + et les -, les * et / sont : un chiffre * un nombre compris entre -99 et 99.
    En difficulté difficile (difficulté = 2), pour les - et +, les nombres sont relatifs avec 2 chiffres max après la virgule, les * et / sont : un nombre compris entre -99 et 99 * un nombre compris entre -99 et 99.
    
    :param difficulte: La difficulte du calcul mental. C'est un entier compris entre 0 et 2.
    :return: Un calcul mental, sous forme de str.
    :return: L'operation liée au calcul, sous forme de str.
    """
    try:
        assert type(difficulte) == int
        assert difficulte >= 0 and difficulte < 3
    except:
        return None
    
    calcul = ''

    if difficulte == 0 :
        
        n1 = random.randint(0, 10)
        n2 = random.randint(0, 10)
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '-' :
            while n1 < n2 :
                n1 = random.randint(0, 10)
                n2 = random.randint(0, 10)
            calcul = str(n1) + '-' + str(n2)
            
        if operation == '/' :
            n1 = random.randint(1, 10)
            dividende = n1*n2
            calcul = str(dividende) + '/' + str(n1)
            
        elif operation == '+' or operation == '*' :
            calcul = str(n1) + operation + str(n2)
            
    
    if difficulte == 1 :
        
        n1 = random.randint(-99, 99)
        n2 = random.randint(-99, 99)
        operation = random.choice(['+', '-', '*', '/'])
            
        if operation == '/' :
            while n1 == 0 :
                n1 = random.randint(-99, 99)
            n2 = random.randint(2, 10)
            dividende = n1*n2
            calcul = str(dividende) + '/' + str(n1)
            
        if operation == '*' :
            n1 = random.randint(2, 10)
            if n2 < 0 :
                calcul = str(n1) + '*' + '(' + str(n2) + ')'
            else :
                calcul = str(n1) + '*' + str(n2)
            
        elif operation == '+' or operation == '-' :
            if n2 < 0 :
                calcul = str(n1) + operation + '(' + str(n2) + ')'
            else :
                calcul = str(n1) + operation + str(n2)
        
        
    if difficulte == 2 :
        
        n1 = random.randint(-100, 99) + round(random.random(), 2)
        n2 = random.randint(-100, 99) + round(random.random(), 2)
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '*' :
            n1 = random.randint(-99, 99)
            n2 = random.randint(-99, 99)
            if n2 < 0 :
                calcul = str(n1) + '*' + '(' + str(n2) + ')'
            else :
                calcul = str(n1) + '*' + str(n2) 
        
        if operation == '/' :
            n1 = random.randint(-99, 99)
            while n1 == 0 :
                n1 = random.randint(-99, 99)
            n2 = random.randint(-99, 99)
            dividende = n1*n2
            calcul = str(dividende) + '/' + str(n1)
            
        else : 
            if n2 < 0 :
                calcul = str(n1) + operation + '(' + str(n2) + ')'
            else :
                calcul = str(n1) + operation + str(n2) 
                
        
    return calcul, operation
              
def reponses_qcm(calcul:str, difficulte:int, operation:str)-> list :
    
    """
    Cette fonction genere les reponses a affichier dans le mode qcm.
    Elle genere 3 reponses fausses en plus de la vrai reponse.
    Selon la difficulté les fausses reponses sont plus ou moins eloignés de la vrai reponse

    :param calcul: un calul generé aleatoirement
    :param difficulte: La difficulte du calcul mental, peut être difficile, normal, facile
    :return: une liste de reponces (melangé afin que la bonne reponse ne soit pas toujours au meme index)
    """
    
    try:
        assert type(calcul) == str
        assert type(difficulte) == int
        assert difficulte >= 0 and difficulte <= 3
    except:
        return None

    bonne_reponse = round(eval(calcul), 2)
    reponses = [bonne_reponse]
    
    if difficulte == 0:
        fausse_minimale = eval(calcul) - 10
        fausse_maximale = eval(calcul) + 10
        fausses = [round(random.uniform(fausse_minimale , fausse_maximale),0) for i in range (3)]

    if difficulte == 1:
        fausse_minimale = eval(calcul) - 30
        fausse_maximale = eval(calcul) + 30
        fausses = [round(random.uniform(fausse_minimale , fausse_maximale),0) for i in range (3)]
        
    if difficulte == 2:
        fausse_minimale = eval(calcul) - 50
        fausse_maximale = eval(calcul) + 50
        if operation == "+" or operation == "-" :
            fausses = [round(random.uniform(fausse_minimale , fausse_maximale),2) for i in range(3)]
        else :
            fausses = [round(random.uniform(fausse_minimale, fausse_maximale),0) for i in range(3)]
    for i in range(3) :
        
        
        while fausses[i] == bonne_reponse or fausses[0] == fausses[1] or fausses[0] == fausses[2] or fausses[1] == fausses[2] :
            if difficulte == 2:
                if operation == "+" or operation == "-" :
                    fausses = [round(random.uniform(fausse_minimale , fausse_maximale),2) for i in range(3)]
                else :
                    fausses = [round(random.uniform(fausse_minimale, fausse_maximale),0) for i in range(3)]
            else :
                fausses = [round(random.uniform(fausse_minimale , fausse_maximale),0) for i in range (3)]
                     
    reponses.extend(fausses)
    random.shuffle(reponses)
    try:
        assert len(reponses) == 4
    except:
        return None
    return reponses    
      
def verifier_reponse(reponse_utilisateur:str, calcul:str)-> str:
    
    """
    Cette fonction vérifie la réponse donnée par l'utilisateur.
    
    :param reponse_utilisateur: La réponse donnée.
    :param calcul: Le calcul mental auquel l'utilisaateur a repondu.
    :return: True si la reponse est juste, sinon la bonne réponse.
    """
    try:
        assert type(reponse_utilisateur) == str
        assert type(calcul) == str
        bonne_reponse = round(eval(calcul),2)
    except:
        return None

    try :
        if round(float(reponse_utilisateur), 2) == round(bonne_reponse, 2) :
            return "Bravo !"
        elif round(float(reponse_utilisateur), 2) != round(bonne_reponse, 2) :
            return "Raté, la bonne réponse était : " + str(bonne_reponse)
    except :
        return "Ecrivez juste un nombre"

def enregistrer_score(nom:str, score:str) :
    
    """
    Cette fonction enregistre les scores des joueurs dans un fichier csv score.csv. 
    Si le joueur a fait un meilleur score, la ligne du tableau correspondant à son pseudo est modifiée. 
    Si le joueur donne un pseudo inconnu, une nouvelle ligne est créée à la fin du tableau.

    :param nom: Le nom entré par l'utilisateur
    :param score: Le score obtenue par l'utilisateur
    """
    """    
    try:
        assert type(nom) == str
        assert type(score) == str
    except:
        return
    """
    fichier_r = open('static/Score.csv', 'r', encoding = 'utf-8')
    modifier = False
    new = ""
    print(nom)
    nom = nom.replace(','," ") # dans le cas ou des malin mettent des vigules dans leur nom et ruinent le classement
    
    for ligne in fichier_r :
        if nom in ligne :
            score_ligne = ligne.split(',')[1]
            if int(score) > int(score_ligne) :
                ligne = ligne.replace(str(score_ligne), str(score)) + "\n"
                new = new + ligne
                modifier = True
            else : 
                new = new + ligne
                modifier = True
        elif nom not in ligne :
            new = new + ligne
            
    if modifier == False :
        ligne = "\n" + nom + ',' + str(score)
        new = new + ligne

    fichier_r.close()
    fichier_w = open('static/Score.csv', 'w', encoding = 'utf-8')
    fichier_w.write(new)
    fichier_w.close()
    return

def meilleur_score(nom:str)->str :
    """
    Cette fonction trouve le meileur score d'un joueur dans le tableau score.csv.

    :param nom: Le nom entré par l'utilisateur
    :return: Le meilleur score detenu par l'utilisateur
    """

    try:
        assert type(nom) == str
    except:
        return

    fichier_r = open('static/Score.csv', 'r', encoding = 'utf-8')
    for ligne in fichier_r :
        nom_ligne = ligne.split(',')[0]
        if nom == nom_ligne :
            return "Votre meilleur score est : " + ligne.split(',')[1]
    return 'Vous êtes anonyme'
    
def trier_csv() :
    """
    Cette fonction écrit les 10 meilleurs scores de Score.csv dans Score_classement.csv, en les triant par ordre décoissant.
    """
    fichier_r = open('static/Score.csv', 'r', encoding = 'utf-8')
    fichier_reader = csv.reader(fichier_r)
    table = []
    comptage_ligne = 0
    for ligne in fichier_reader :
        comptage_ligne += 1
        table.append(ligne)
        
    for i in range(len(table)) :
        m = i
        for j in range(i+1, len(table)) :
            if int(table[j][1]) < int(table[m][1]) :
               m = j
        x = table[i]
        table[i] = table[m]
        table[m] = x
        
    table.reverse()
    if len(table) > 10 :
        table = [table[i] for i in range(10)]
    
    fichier_w = open('static/Score_classement.csv', 'w', encoding = 'utf-8')
    fichier_writer = csv.writer(fichier_w)
    for i in range(len(table)) :
        fichier_writer.writerow(table[i])
