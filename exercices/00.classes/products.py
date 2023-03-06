class Product :
    def __init__(self, cout, prix, marque) :
        self.cost = cout
        self.price = prix
        self.marque = marque

class Meubles (Product):
    def __init__(self, cout, prix, marque, materiau, couleur, dimension) :
        super().__init__(cout, prix, marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimension = dimension

        
class Canape (Meubles):
    def __init__(self, cout, prix, marque, materiau, couleur, dimension, nom) :
        super().__init__(cout, prix, marque, materiau, couleur, dimension)
        self.nom = nom

    def afficher_attributs (self) :
        print("Détails :", self.cost, self.price, self.marque, self.materiau, self.couleur, self.dimension, self.nom)


class Chaise (Meubles):
    def __init__(self, cout, prix, marque, materiau, couleur, dimension, nom) :
        super().__init__(cout, prix, marque, materiau, couleur, dimension)
        self.nom = nom

    def afficher_attributs (self) :
        print("Détails :", self.cost, self.price, self.marque, self.materiau, self.couleur, self.dimension, self.nom)


class Table (Meubles) :
    def __init__(self, cout, prix, marque, materiau, couleur, dimension, nom) :
        super().__init__(cout, prix, marque, materiau, couleur, dimension)
        self.nom = nom

    def afficher_attributs (self) :
        print("Détails :", self.cost, self.price, self.marque, self.materiau, self.couleur, self.dimension, self.nom)    



# Création d'une instance de chaque classe
canape1 = Canape('1000 €','2 000 €', 'OKLM','Cuir', 'Blanc', '200x100x80 cm', 'Canape')
canape2 = Canape ('800 €', '1 600 €', 'SIESTA', 'Tissu', 'Bleu', '150x90x70 cm', 'Canape')
chaise1 = Chaise('50 €', '100 €', 'PEPOUSE', 'Plastique', 'Rouge', '50x50x70 cm', 'chaise')
chaise2 = Chaise('75 €', '150 €', 'PEPOUSE', 'Metal', 'Gris', '60x60x80 cm', 'chaise')
table1 = Table ('350 €', '700 €', 'TEX', 'Verre', 'Transparent', '120x60x75 cm', 'table')
table2 = Table ('250 €', '500 €', 'TEX', 'Bois', 'Chêne', '150x80x75 cm', 'table')

canape1.afficher_attributs()
canape2.afficher_attributs()
chaise1.afficher_attributs()
chaise2.afficher_attributs()
table1.afficher_attributs()
table2.afficher_attributs()
