from tkinter import *
from pylab import figure, axes, linspace, plt, sqrt, log, exp

def drawGraph(func):
    ax = axes()
    x = linspace(0, 100, 10000)
    ax.plot(x, eval(func))
    plt.show()

def addNum(arg):
    global affichage, label_affichage
    if affichage == "0":
        affichage = ""
    affichage+=arg
    label_affichage.config(text=affichage)
    return

def egal():
    global affichage, label_affichage
    if affichage != "":
        affichage = eval(affichage)
        label_affichage.config(text=affichage)
        affichage = ""

def reset():
    global affichage, label_affichage
    label_affichage.config(text=0)
    affichage = ""

def gestEvent(evt):
    if evt.char == "+":
        addNum("+")
    elif evt.char == "-":
        addNum("-")
    elif evt.char == "*":
        addNum("*")
    elif evt.char == "/":
        addNum("/")
    elif evt.char == ".":
        addNum(".")
    elif evt.char ==  "\r":
        egal()
    else:
        for i in range(10):
            if evt.char == str(i):
                addNum(str(i))
    

racine = Tk()
racine.title("calculatrice")
#racine.geometry("250x150+100+100")
racine.bind("<Key>", gestEvent)

affichage = "0"



#CRéation des widgets
bouton_add = Button(racine, text="+", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("+"))
bouton_moins = Button(racine, text="-", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("-"))
bouton_diviser = Button(racine, text = "/", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("/"))
bouton_multipli = Button(racine, text = "*", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("*"))
bouton0 = Button(racine, text = "0", width = 18, activebackground = "Black", activeforeground = "White", command = lambda: addNum("0"))
bouton1 = Button(racine, text = "1", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("1"))
bouton2 = Button(racine, text = "2", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("2"))
bouton3 = Button(racine, text = "3", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("3"))
bouton4 = Button(racine, text = "4", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("4"))
bouton5 = Button(racine, text = "5", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("5"))
bouton6 = Button(racine, text = "6", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("6"))
bouton7 = Button(racine, text = "7", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("7"))
bouton8 = Button(racine, text = "8", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("8"))
bouton9 = Button(racine, text = "9", width = 5, activebackground = "Black", activeforeground = "White", command = lambda: addNum("9"))
bouton_egal = Button(racine, text="=", width = 38, activebackground = "Black", activeforeground = "White", command = egal)
bouton_supprime = Button(racine, text="C", width = 12, activebackground = "Black", activeforeground = "White", command = reset)
label_affichage = Label(racine, text=affichage, bg="black", fg = "white", width = 25)
bouton_point = Button(racine, text=".", width = 10, activebackground = "Black", activeforeground = "White", command = lambda: addNum("."))
bouton_graphe_carre = Button(racine, text = "Courbe x²", width = 12, activebackground = "Black", activeforeground = "White", command = lambda: drawGraph("x**2"))
bouton_graphe_racine_carre = Button(racine, text = "Courbe racine(x)", width = 12, activebackground = "Black", activeforeground = "White", command = lambda: drawGraph("sqrt(x)"))
bouton_graphe_exp = Button(racine, text = "Courbe exp(x)", width = 12, activebackground = "Black", activeforeground = "White", command = lambda: drawGraph("exp(x)"))
bouton_graphe_log = Button(racine, text = "Courbe log(x)", width = 12, activebackground = "Black", activeforeground = "White", command = lambda: drawGraph("log(x)"))


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
bouton_egal.grid(column=0, row=5, columnspan=5)
bouton_supprime.grid(column=4, row=0)
label_affichage.grid(column=0,row=0, columnspan=4)
bouton_point.grid(column=4, row=3)
bouton_graphe_carre.grid(column=4, row=1)
bouton_graphe_racine_carre.grid(column=4, row=2)
bouton_graphe_exp.grid(column=4,row = 3)
bouton_graphe_log.grid(column=4,row = 4)




racine.mainloop()