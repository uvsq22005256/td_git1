from tkinter import *

def addNum(arg):
    global affichage, label_affichage
    if affichage == "0":
        affichage = ""
    affichage+=arg
    label_affichage.config(text=affichage)
    return

def egal():
    global affichage, label_affichage
    affichage = eval(affichage)
    label_affichage.config(text=affichage)
    affichage = ""

def reset():
    global affichage, label_affichage
    label_affichage.config(text=0)
    affichage = ""

racine = Tk()
racine.title("calculatrice")
racine.geometry("250x250+100+100")

affichage = "0"


#CRéation des widgets
bouton_add = Button(racine, text="+", width = 5, command = lambda: addNum("+"))
bouton_moins = Button(racine, text="-", width = 5, command = lambda: addNum("-"))
bouton_diviser = Button(racine, text = "/", width = 5, command = lambda: addNum("/"))
bouton_multipli = Button(racine, text = "*", width = 5, command = lambda: addNum("*"))
bouton0 = Button(racine, text = "0", width = 5, command = lambda: addNum("0"))
bouton1 = Button(racine, text = "1", width = 5, command = lambda: addNum("1"))
bouton2 = Button(racine, text = "2", width = 5, command = lambda: addNum("2"))
bouton3 = Button(racine, text = "3", width = 5, command = lambda: addNum("3"))
bouton4 = Button(racine, text = "4", width = 5, command = lambda: addNum("4"))
bouton5 = Button(racine, text = "5", width = 5, command = lambda: addNum("5"))
bouton6 = Button(racine, text = "6", width = 5, command = lambda: addNum("6"))
bouton7 = Button(racine, text = "7", width = 5, command = lambda: addNum("7"))
bouton8 = Button(racine, text = "8", width = 5, command = lambda: addNum("8"))
bouton9 = Button(racine, text = "9", width = 5, command = lambda: addNum("9"))
bouton_egal = Button(racine, text="=", width = 5, command = egal)
bouton_supprime = Button(racine, text="C", width = 5, command = reset)
label_affichage = Label(racine, text=affichage, bg="orange")
bouton_point = Button(racine, text=".", width = 5, command = lambda: addNum("."))

#affichage des 
bouton_add.grid(column=0,row=1)
bouton_moins.grid(column=0, row = 2)
bouton_diviser.grid(column=0, row=3)
bouton_multipli.grid(column=0, row=4)
bouton0.grid(column=1, row=4, columnspan=3)
bouton1.grid(column=3,row=3)
bouton2.grid(column=2,row=3)
bouton3.grid(column=1,row=3)
bouton4.grid(column=3,row=2)
bouton5.grid(column=2,row=2)
bouton6.grid(column=1,row=2)
bouton7.grid(column=3,row=1)
bouton8.grid(column=2,row=1)
bouton9.grid(column=1,row=1)
bouton_egal.grid(column=4, row=4)
bouton_supprime.grid(column=4, row=0)
label_affichage.grid(column=0,row=0, columnspan=3)
bouton_point.grid(column=4, row=3)




racine.mainloop()