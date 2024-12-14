class Noeud:
    def __init__(self,g,v,d):
        self.gauche=g
        self.valeur=v
        self.droit=d
    #def __str___(self):
      #  print(self.gauche,',(',self.valeur,'),',self.droit)




def inserer(x,a):
    if a is None:
        print(x)
        return Noeud(None,x,None) 
    elif x<a.valeur:
        print('1')
        return Noeud(inserer(x,a.gauche),a.valeur,a.droit)
    else:
        print('1')
        return Noeud(a.gauche,a.valeur,inserer(x,a.droit))
        
    

compte=0
lst5=[7,9,3,5,4,1] #9
lst3=[1,3,4,5,7,9]#15
lst=[5,3,1,6,2,4]#11
a=None
for v in lst:
    a=inserer(v,a)
def lou (a):
    if a is True:
        print("lou-anne the best")


a=True
lou(a)



