class Lampe:
    def __init__(self):
        self.allumee=False
    
    def isOn(self):
        onOff=input("allumée ou eteind ? ")
        if onOff =="allumée":
            self.allumee=True
        elif onOff =="eteind":
            self.allumee=False
        else:
            print("erreure")
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