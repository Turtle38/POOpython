class Lampe:
    def __init__(self):
        self.allumee=False
    
    def isOn(self):
        if input("allumée ou eteind: ")=="allumée":
            self.allumee=True
        else:
            self.allumee=False
    
    def lampePropriete(self):
        if self.allumee==False:
            print("éteind")
        else:
            print("allumée")

while(True):
    lampe=Lampe()
    lampe.isOn()
    lampe.lampePropriete()
input()