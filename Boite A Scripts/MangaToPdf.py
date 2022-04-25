import os

path = "./"
liste_dossier = []
for r, d, f in os.walk(path):
    liste_dossier.append(d)

for i in liste_dossier:
    fichiers = " "
    for r, d, f in os.walk(i):
        for file in f:
            if ".jpeg" in file:
                fichiers += f" {f}"
    os.system(f"gm {fichiers} {tome}.pdf")
