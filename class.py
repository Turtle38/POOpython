class Person:
    ####variables de la classe ici####
    name = ""
    #################################


    ####fonctions de la classe ici####
    def hello():
        print("bonjour twa !")
    
    def bye():
        print("au revoir twa ;)")
    
    #################################


######ecrire un programme qui demande au gens gens la taille et la couleur de la table####
class Table:

    #######fontions######
    def __init__(self):
        self.perimetre="0"
        self.couleur="default"
    def setPerimetre(self):
        self.perimetre=input("entres le perimetre de la table: ")

    def setCouleur(self):
        self.couleur=input("donnes la couleure de la table: ")
    
    #Declarer une fonction qui affiche les propriétés de la table :)
    def afficherPropriete(self):
        print("vous avez créer une table "+self.couleur+" avec un perimetre de "+self.perimetre+" !!")


table = Table()
table.setPerimetre()
table.setCouleur()
table.afficherPropriete()


input()