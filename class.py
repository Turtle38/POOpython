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
    def __init__():
        self.perimetre="0"
        self.couleur="default"
    def perimetre():
        perimetre=input("entres le perimetre de la table: ")

    def couleur():
        couleur=input("donnes la couleure de la table: ")
    
    #Declarer une fonction qui affiche les propriétés de la table :)
    def afficherPropriete():
        print("vous avez créer ube table"+couleur+"avec un perimetre de"+perimetre+"!!")


table = Table()
table.perimetre()
table.couleur()
table.afficherPropriete()


input()