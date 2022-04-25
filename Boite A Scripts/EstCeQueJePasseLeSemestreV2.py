listNotes = [0 for i in range(22)]
listeComp = []
jePasse = True
ressoureces = 12
semestre = 0
#S1
matriceCoef =  [[40,0 ,0 ,0 ,0 ,0 ,0,0,42,12,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ,0 ,0 ,0,0],
                [0 ,40,0 ,0 ,0 ,0 ,0,0,24,0 ,3 ,3 ,0 ,15,15,0 ,0 ,0 ,0 ,0 ,0,0],
                [0 ,0 ,40,0 ,0 ,0 ,0,0,0 ,0 ,21,21,0 ,0 ,0 ,0 ,0 ,12,6 ,0 ,0,0],
                [0 ,0 ,0 ,40,0 ,0 ,0,0,0 ,0 ,0 ,0 ,36,18,0 ,0 ,6 ,0 ,0 ,0 ,0,0],
                [0 ,0 ,0 ,0 ,40,0 ,0,0,0 ,18,0 ,0 ,0 ,0 ,0 ,27,0 ,0 ,15,0 ,0,0],
                [0 ,0 ,0 ,0 ,0 ,40,0,0,0 ,5 ,0 ,0 ,0 ,0 ,0 ,11,11,11,11,11,0,0]]


while semestre not in [1,2]:
    semestre = int(input("donne le semestre stp (1 ou 2) : "))

if semestre == 2:
    ressoureces = 14
    listNotes[6] = float(input(f"Saisis la note 'portfolio' : "))
    #S2
    matriceCoef =  [[38,0 ,0 ,0 ,0 ,0 ,2 ,0,21,21,12,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,6 ,0 ],
                    [0 ,38,0 ,0 ,0 ,0 ,2 ,0,15,0 ,0 ,12,0 ,0 ,21,0 ,12,0 ,0 ,0 ,0 ,0 ],
                    [0 ,0 ,38,0 ,0 ,0 ,2 ,0,0 ,0 ,0 ,36,15,0 ,0 ,0 ,0 ,0 ,0 ,6 ,3 ,0 ],
                    [0 ,0 ,0 ,38,0 ,0 ,2 ,0,0 ,0 ,0 ,0 ,0 ,30,0 ,12,0 ,12,0 ,6 ,0 ,0 ],
                    [0 ,0 ,0 ,0 ,38,0 ,2 ,0,0 ,3 ,6 ,0 ,0 ,0 ,6 ,0 ,0 ,30,0 ,6 ,9 ,0 ],
                    [0 ,0 ,0 ,0 ,0 ,38,2 ,0,0 ,4 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,17,17,11,11]]
    
# Ressoureces
for i in range(ressoureces):
    indice = 8 + i
    listNotes[indice] = float(input(f"Saisis la note de R{semestre}.{i+1} : "))

# Saes
for i in range(6):
    listNotes[i] = float(input(f"Saisis la note de S{semestre}.{i+1} : "))

for comp in matriceCoef:
    competance = 0
    for i in range(len(listNotes)):
        competance += comp[i] * listNotes[i]
    competance = competance / 100
    if competance < 10:
        jePasse = False
    listeComp.append(competance)

print(30*'-')
for i in range(len(listeComp)):
    print(f"note de la competance {i+1} : {round(listeComp[i],2)}")
    moyenne = 0
    for i in listeComp:
        moyenne += i
    moyenne = moyenne / len(listeComp)
print(f"ta moyenne est de : {round(moyenne,2)}")

if jePasse:
    print("Tkass bg t'as un avenir")
else:
    print("envisage la reconversion kebab")