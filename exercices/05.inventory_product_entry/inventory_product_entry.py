'''Nous allons a présent créer une classe InventoryProductEntry qui a pour role de représenter 
une entrée d'inventaire pour un produit spécifique.
Après avoir créer les différentes classes qui modélisent les produits de notre magasin, 
nous devons créer du code qui permet de gérer nos produits et leur inventaire.
Cette classe nous permettra de stocker des informations telles que la quantité en stock, 
les revenues et les dépenses liées à ce produit.
Donc, elle permet de gérer le stock lié à un seul produit.'''
# Vous allez créer une classe InventoryProductEntry qui a pour role de
# représenter une entrée d'inventaire pour un produit spécifique.


class InventoryProductEntry:
    # Initialisation de la classe, en prenant en argument un objet Product et une quantité initiale
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = int(quantity)

        """
        'product' : un objet de type produit qui rassemble les différents attributs et caractéristiques de ce dernier
        'quantity' : un entier qui représente le nombre des pièces du produit en question
        """
        # Initialisation des variables
        self.sales = 0
        self.expenses = 0
        """
        Vous devez initialiser deux variables. 
        la variable 'sales' qui stocke le total des revenus des ventes du produit
        la variable 'expenses' qui stocke le total des dépenses pour restocker le produit
        """
    # Méthode Sell
    """
    La méthode sell est utilisée pour retirer la quantité vendue du produit depuis le stock.
    Elle met également à jour les ventes totales pour le produit.
    """

    def sell(self, quantity):
        # Avant de mettre à jour l'état du stock du produit, on doit vérifier si on a déjà une quantité suffisante à vendre.
        if self.quantity < quantity:
            print('Le stock du produit ', [self.product], ' est insuffisant')
            return (False)
        else:
            self.quantity -= quantity
            self.sales += quantity*self.price
            return (True)

    """
        En utilisant des conditions, vérifier: 

        SI la quantité en stock est inférieure à la quantité demandée:
            Afficher "Le stock du produit [nom du produit] est insuffisant."
            Retourner Faux
        SINON:
            Réduire la quantité en stock par la quantité demandée
            Ajouter le revenue total de la vente à la variable 'sales' en multipliant la quantité vendue par le prix du produit
            Retourner Vrai
        
    """

    # Méthode Restock
    """
    La méthode restock est utilisée pour augmenter la quantité en stock lorsqu'un nouveau stock de produit est reçu. 
    Elle met également à jour les dépenses totales pour restocker ce produit.
    """

    def restock(self, quantity):
        self.quantity += quantity
        self.expenses += quantity*self.cost
    """
        Ajouter la quantité reçue à la quantité en stock
        Ajouter le coût total de la nouvelle quantité reçue  à la variable 'expenses' en multipliant la quantité reçue par le coût du produit
    """

    # Méthode repr
    """
    La méthode repr est utilisée pour fournir une représentation en chaîne de caractères de l'objet InventoryProductEntry, 
    qui contient des informations utiles telles que le nom du produit, la marque, la quantité en stock et le prix du produit.

    """

    def __repr__(self):
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.
        return (self.name, self.marque, self.quantity, self.price)
