import random

class Adversaire:
    
    def jouer(self):
        choixADV = random.randint(1,3)
        return choixADV

class Joueur:
    def jouer2(self):
        choix = int(input("1 pour pierre, 2 pour papier et 3 pour ciseau: "))
        return choix

class Jeu:
    score = 0
    scoreADV = 0
    def comparer(self,choix,choixADV):
        if choixADV == 1 and choix == 2:
            print("l'adversaire à choisi pierre , il a donc perdu")
            self.score = self.score + 1
        elif choix == 1 and choixADV == 2:
            print("l'adversaire à choisi papier, il a donc gagné")
            self.scoreADV = self.scoreADV + 1
        elif choix == 2  and choixADV == 3:
            print("l'adversaire a choisi ciseau, il a donc gagné")
            self.scoreADV = self.scoreADV + 1
        elif choix == 3 and choixADV == 2:
            print("l'adversaire a choisi papier,il a donc perdu")  
            self.score =self.score + 1
        elif choix == 1 and choixADV == 3:
            print("l'adversaire a choisi ciseau, il a donc perdu")
            self.score = self.score + 1 
        elif choix == 3 and choixADV == 1:
            print("l'adversaire a choisi pierre, il a donc gagné")
            self.scoreADV = self.scoreADV + 1
        elif choix == choixADV:
            print("égalité")
        else:
            print("error")

adversaire = Adversaire()
joueur = Joueur()
jeu = Jeu()



while(jeu.score != 3 and jeu.scoreADV != 3):
   
    jeu.comparer(joueur.jouer2(),adversaire.jouer() )
    print("joueur = "+ str(jeu.score) + "adversaire = " + str(jeu.scoreADV))


