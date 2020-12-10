from tkinter import *

racine = Tk()
racine.title("calculatrice")

affichage = "0"

bouton_add = Button(racine, text="+")
bouton_moins = Button(racine, text="-")
bouton_diviser = Button(racine, text = "/")
bouton_multipli = Button(racine, text = "*")
bouton0 = Button(racine, text = "0")
bouton1 = Button(racine, text = "1")
bouton2 = Button(racine, text = "2")
bouton3 = Button(racine, text = "3")
bouton4 = Button(racine, text = "4")
bouton5 = Button(racine, text = "5")
bouton6 = Button(racine, text = "6")
bouton7 = Button(racine, text = "7")
bouton8 = Button(racine, text = "8")
bouton9 = Button(racine, text = "9")
bouton_egal = Button(racine, text="=")
bouton_supprime = Button(racine, text="C")
label_affichage = Label(racine, text=affichage, bg="orange")
bouton_point = Button(racine, text=".")

bouton_add.grid(column=0,row=1)
bouton_moins.grid(column=0, row = 2)
bouton_diviser.grid(column=0, row=3)
bouton_multipli.grid(column=0, row=4)
bouton0.grid(column=3, row=4)
bouton1.grid(column=3,row=3)
bouton2.grid(column=2,row=3)
bouton3.grid(column=1,row=3)
bouton4.grid(column=3,row=2)
bouton5.grid(column=2,row=2)
bouton6.grid(column=1,row=2)
bouton7.grid(column=3,row=1)
bouton8.grid(column=2,row=1)
bouton9.grid(column=1,row=1)
bouton_egal.grid(column=1, row=4)
bouton_supprime.grid(column=2, row=4)
label_affichage.grid(column=0,row=0, columnspan=3)
bouton_point.grid(column=0, row=5)



racine.mainloop()