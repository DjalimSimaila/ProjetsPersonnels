from flask import Flask, render_template, request
from fonctions import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Acceuil.html")

@app.route("/commencer_classique/", methods = ['POST'])
def commencer():
    difficulte = int(request.form['radio'])
    calcul_entier = creer_calcul(difficulte)
    calcul = calcul_entier[0]
    operation = calcul_entier[1]
    numero = 1
    calcul_juste = 0
    return render_template("Calcul.html",difficulte=difficulte, calcul=calcul, numero = numero,calcul_juste=calcul_juste)

@app.route("/commencer_qcm/", methods = ['POST'])
def commencer_qcm():
    difficulte = int(request.form['radio'])
    calcul_entier = creer_calcul(difficulte)
    calcul = calcul_entier[0]
    operation = calcul_entier[1]
    reponces =  reponses_qcm(calcul,difficulte,operation)
    numero = 1
    calcul_juste = 0
    rep1 = float(reponces[0])
    rep2 = float(reponces[1])
    rep3 = float(reponces[2])
    rep4 = float(reponces[3])
    return render_template("Calcul_qcm.html", calcul=calcul,difficulte=difficulte, rep1=rep1, rep2=rep2, rep3=rep3, rep4=rep4, numero=numero,calcul_juste=calcul_juste, operation=operation)

@app.route("/suivant/", methods = ['POST'])
def suivant():
    try:
        reponse = request.form['resultat']
    except:
        reponse = ''
    calcul = request.form['calcul']
    operation = request.form['operation']
    verification = verifier_reponse(reponse, calcul)
    calcul_juste = int(request.form['calcul_juste'])
    if verification == "Bravo !" :
        calcul_juste += 1
    difficulte = int(request.form['difficulte'])
    
    calcul_entier = creer_calcul(difficulte)
    calcul = calcul_entier[0]
    operation = calcul_entier[1]
    
    mode = request.form['type']
    numero = int(request.form['numero'])
    if verification == "Ecrivez juste un nombre" :
        numero -= 1
        calcul = request.form['calcul']
        operation = request.form['operation']
    while numero < 2 :
        if mode == "qcm":
            numero += 1
            reponces =  reponses_qcm(calcul,difficulte,operation)
            rep1 = float(reponces[0])
            rep2 = float(reponces[1])
            rep3 = float(reponces[2])
            rep4 = float(reponces[3])
            return render_template("Calcul_qcm_suivant.html",difficulte=difficulte, calcul=calcul,verification=verification, rep1=rep1, rep2=rep2, rep3=rep3, rep4=rep4,numero = numero,calcul_juste=calcul_juste)
        else :
            numero += 1
            return render_template("Calcul_suivant.html",difficulte=difficulte, calcul=calcul, verification=verification, numero=numero, calcul_juste=calcul_juste)
    return render_template("Resultat.html",calcul_juste=calcul_juste)

@app.route('/resultat/', methods=['POST'])
def resultat():
    score = int(request.form['score'])
    nom = request.form['nom']
    
    nom = nom.strip()
    if len(nom) > 10 :
        erreur = 'Trop de caractères'
        calcul_juste = request.form['score']
        return render_template("Resultat.html",calcul_juste=calcul_juste, erreur=erreur)
    if len(nom) > 0 :
        print(nom)
        enregistrer_score(nom, score)
    ms = meilleur_score(str(nom))
    return render_template('Classement.html', nom=nom, ms=ms)
    
@app.route('/classement', methods=['GET', 'POST'])
def classement() :
    trier_csv()
    return render_template('Classement.html')

if __name__ == "__main__":
    app.run(host="localhost", port = 5002,debug=True)
