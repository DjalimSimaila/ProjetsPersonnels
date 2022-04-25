#!/bin/python3

"""
Ce code n'avait pas vocation a etre lu et/ou partagé
Ne veuillez pas prendre compte des nom de fonctions 
et des messages que ce parser retourne
"""

import os
import sys
import requests

# lets go to hell together bs4
from bs4 import BeautifulSoup

class VoleurDeManga: 
    def __init__(self):
        self.path = "./"
        self.nomSwag = "un manga i guess"
        self.pageManga = None
        self.listeImage = []
        self.nombreTomes = 0
        self.nombrePages = 0

    def __str__(self):
        return ("j'ai la gueule d'un programe java la con de tes morts")

    def idiotproofing(self):
        if len(sys.argv) > 2: self.pageManga = sys.argv[sys.argv.index("-l") + 1]
        while True:
            if self.pageManga is None:
                print("donne le lien de la page de ton manga exemple : https://sushi-scan.su/manga/black-butler/ ")
                self.pageManga = input("le lien de ton manga stp : ")
            if requests.get(self.pageManga).status_code == 200 : return
            self.pageManga = None

    def jeSaisPasCommentTappeller(self):
        """
        """
        self.idiotproofing()
        assiete = self.trouvonsLesTomes()
        self.path += f'"{self.nomSwag}"/'
        print(f"telechargement de {self.nomSwag}")
        self.purificateurDassiete(assiete)
        print("fait, passons aux telechargements                                  ")
        self.telechargeMoiLesImages()

    def purificateurDassiete(self, assiete : list):
        """
        """
        cpt = 0
        for sauce in assiete:
            cpt += 1
            self.listeImage.append([])
            print(f"recuperation des liens des images du tome {cpt}",end='\r')
            recette = requests.get(sauce.find("a")["href"])
            soupe = BeautifulSoup(recette.content,"html.parser")
            for legume in soupe.find("div",id="readerarea").find_all('img'):
                self.listeImage[-1].append(legume["src"])
            self.nombrePages += len(self.listeImage[-1])
        self.listeImage.reverse()
        return
        
    def trouvonsLesTomes(self):
        """
        """
        assiete = []
        recette = requests.get(self.pageManga)
        soupe = BeautifulSoup(recette.content,"html.parser")
        self.nomSwag = soupe.title.string.split('–')[0]
        for sauce in soupe.find_all("li"):
            if sauce.find('div',"eph-num"):
                assiete.append(sauce)
        assiete.pop(0)
        return assiete

    def telechargeMoiLesImages(self):
        """
        """
        pageVues = 0
        for tome in range(len(self.listeImage)):
            if not os.path.exists(self.path+f"{tome + 1}"): os.system(f"mkdir -p {self.path}{tome + 1}")
            pageActuelle = 0
            for page in self.listeImage[tome]:
                pageActuelle += 1
                pageVues += 1
                if os.path.exists("{}/{}/{}".format(self.path,tome+1,page.split('/')[-1])): continue
                page_image = os.system(f"wget -q --directory-prefix {self.path}{tome+1} {page}")
                print(f'[{int(pageVues/self.nombrePages * 50) * "#"}{(50-int(pageVues/self.nombrePages * 50)) * " "}] page {pageActuelle} du tome {tome+1}                        ', end='\r')


if __name__ == "__main__":
    manga = VoleurDeManga()
    manga.jeSaisPasCommentTappeller()
