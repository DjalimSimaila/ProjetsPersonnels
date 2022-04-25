from fonctions import *

def test_cree_calcul_aleatoire_facile():
    for i in range(10):
        precedant = creer_calcul(0)
        assert creer_calcul(0) != precedant

def test_cree_calcul_aleatoire_normal():
    for i in range(10):
        precedant = creer_calcul(1)
        assert creer_calcul(1) != precedant

def test_cree_calcul_aleatoire_difficile():
    for i in range(10):
        precedant = creer_calcul(2)
        assert creer_calcul(2) != precedant

def test_cree_calcul_difficulte_str():
    assert creer_calcul("0") == None

def test_cree_calcul_difficulte_invalide():
    assert creer_calcul(4) == None

#-----------------------------------------------------------------#

# Cette fonction est un peu chelou a test, si tu trouve des test a faire
# je suis preneur

#def test_reponces_qcm_simple()
#   assert reponses_qcm("1+1",0,"+")

#-----------------------------------------------------------------#

def test_verifier_reponse_simple_juste():
    assert verifier_reponse("2","1+1") == "Bravo !"

def test_verifier_reponse_simple_faux():
    assert verifier_reponse("11","1+1") == "Raté, la bonne réponse était : 2"

def test_verifier_reponse_lettre():
    assert verifier_reponse("deux","1+1") == "Ecrivez juste un nombre"

def test_verifier_reponse_reponse_type_int():
    assert verifier_reponse(2,"1+1") == None

def test_verifier_reponse_calcul_incorrect():
  assert verifier_reponse("2","1plus1") == None

#-----------------------------------------------------------------#

def test_enregistrer_score_nom_type_int():
   assert enregistrer_score(123,"456") == None

def test_enregistrer_score_score_type_int():
   assert enregistrer_score("test",123) == None

#-----------------------------------------------------------------#
def test_meilleur_score_type_int():
   assert meilleur_score(123) == None

