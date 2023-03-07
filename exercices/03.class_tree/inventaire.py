import json
import os
from unidecode import unidecode
from treelib import Tree

def json_dict_from_file():
    local_path = os.path.dirname(os.path.abspath(__file__))
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    json_str = json.dumps(json_data)
    json_data = (unidecode(json_str))
    json_dict = json.loads(json_data)
    return json_dict

def create_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            # Créer un nouveau noeud pour la clé courante du dictionnaire
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)
        else:
            # Créer un nouveau noeud pour la feuille courante du dictionnaire
            leaf_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)
 # Fonction récursive pour parcourir un dictionnaire Python et créer des noeuds dans un arbre
def recusive_tree_from_json(json_dict, parent_node_id):
    for key, value in dict :
'''Pour chaque clé (class_name) et valeur (class_attrs) dans le dictionnaire :
        Créer un nouveau noeud pour la clé courante du dictionnaire (nom de la classe)
        Ajouter le nouveau noeud en tant que fils du noeud parent

        Si "subclasses" est dans les attributs de la classe en cours (soit : valeur(class_attrs))
            Appeler récursivement la fonction pour créer les sous-noeuds de ce dictionnaire  '''     
 
def main():
'''    Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    Créer l'arbre à partir du dictionnaire Python
    Afficher l'arbre de classes'''
    my_tree = Tree()

    my_tree.create_node(tag="Racine", identifier="racine")

 
    json_dict = json_dict_from_file()
    create_tree_from_dict(my_tree, "racine", json_dict)

    my_tree.show()

if __name__ == '__main__':
    main()