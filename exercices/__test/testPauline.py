class Product:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

class Meuble(Product):
    def __init__(self, marque, modele, annee, nb_portes):
        super().__init__(marque, modele, annee)
        self.nb_portes = nb_portes


#Créer une classe qui comporte une méthode, ajoute des objects de type produits dans une liste et une méthode qui affiche la liste.


class Product :
    