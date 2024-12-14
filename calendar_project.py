import sqlite3
from tkinter import *
from tkcalendar import Calendar
from random import*

def initialisation_bd():
    f = open('calendrier.sql',encoding='utf-8')
    ordres_sql = f.read()
    f.close()

    calendrier_con = sqlite3.connect("calendrier.db")
    calendrier_con.executescript(ordres_sql)
    calendrier_con.close()

#initialisation_bd()

def afficher():
    calendrier_con = sqlite3.connect("calendrier.db")
    for row in calendrier_con.execute("SELECT * FROM evenement;") :
        print(row)
    calendrier_con.close()

afficher()

class Calendrier :
    def __init__(self):
        self.con = None

    def connexion(self):
        self.con = sqlite3.connect("calendrier.db")
        print('connexion en cours....')

    def deconnexion(self):
        self.con = self.con.close()

    def rechercher_jour(self,jour):
        self.connexion()
        j = self.con.execute(f"SELECT tache FROM evenement WHERE '{jour}' = jour ;").fetchall()
        self.deconnexion()
        return j
    

    def add(self,l):
        self.connexion()
        self.con.execute(f"INSERT INTO evenement VALUES {l}")
        print(f"j'ai mis dans la table : {l} ")
        self.con.commit()
        self.deconnexion()
    
    def supr(self,id):
        self.connexion()
        self.con.execute(f"DELETE FROM evenement WHERE id = {id}")
        print("j'ai supprrrr ")
        self.con.commit()
        self.deconnexion()


   
root = Tk()
root.geometry("400x400")
root.title("Calendrier")
root.iconbitmap("logo.png")

frame = Frame(root,bg='#8C968F')
frame2 = Frame(root)
frame3 = Frame (root)

dict_date={}
def add_button():
    t = task.get()
    new_label = Label(root, text=t)
    d, i = grab_date(), str(randint(1000000,8900000))
    dict_date[d]=i
    print(dict_date)
    e=Calendrier()
    e.add((t, d, i))
    task.delete(0,END)
    new_button = Button(frame3, text="     -     ", command=lambda: new_button.pack_forget() + new_label.pack_forget() +e.supr(i))
    new_label.pack()
    new_button.pack()

def grab_date():
    a=cal.get_date()
    
    return a


cal = Calendar(frame, selectmode="day", date_patern='mm/dd/y', year=2024, month= 5)
cal.pack(fill='both',expand=True)

task = Entry(frame2)
task.pack()


btn2 = Button(frame2,text='choisir la date',font='Helvetica',command=grab_date)
btn2.pack()
add_button_button = Button(frame2, text="      Ajouter      ",font='Helvetica', command=add_button)
add_button_button.pack()

frame.pack(expand=YES)
frame2.pack(expand=YES)
frame3.pack(expand=YES)


root.mainloop()
