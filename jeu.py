from tkinter import *
from tkinter import messagebox
import random
import time

root = Tk()#créeation de la fenetre
root.title("Morpion")#nom de la fenetre
root.geometry("534x600")#taille de la fenetre
root.resizable(width=False, height=False)#empechement de redimensionner la fenetre

#variable
playing = 1
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
nbcoup = 0
egaliter = 0
r = IntVar()
r.set("1")


#importation des image utile
rond = PhotoImage(file='rond.png')
croix = PhotoImage(file='croix.png')
rien = PhotoImage(file='rien.png')


#nouvelle partie
def newgame():
    global game, playing, nbcoup,egaliter
    egaliter = 0
    playing = 1
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    nbcoup = 0
    button1['image'] = rien
    button2['image'] = rien
    button3['image'] = rien
    button4['image'] = rien
    button5['image'] = rien
    button6['image'] = rien
    button7['image'] = rien
    button8['image'] = rien
    button9['image'] = rien
    if r.get() == 2 or r.get() ==3:
        playing = 2
        playbot()





def playbot():
    global egaliter
    posL = [] #position libre
    for i in range(len(game)):
        for y in range(len(game[i])):
            if game[i][y]==0:
                posL.append((i,y))
    #IA Facile
    if r.get()== 1 :
        x = posL[random.randint(0,len(posL)-1)]
        buttonPress([x[0],x[1],button[x[0]][x[1]]])

    #IA moyen
    if r.get()==2:
        if nbcoup==0:
            buttonPress([0, 0, button[0][0]])
        elif nbcoup==2:
            if game[2][2]==0:
                buttonPress([2, 2, button[2][2]])
            else:
                buttonPress([2, 0, button[2][0]])

        elif nbcoup==4:
            if game[2][2] == 2:
                if game[1][1]==0:
                    buttonPress([1, 1, button[1][1]])
                elif game[2][0] == 0:
                    buttonPress([2, 0, button[2][0]])
                else:
                    buttonPress([0, 2, button[0][2]])
            else:
                if game[1][0]==0:
                    buttonPress([1, 0, button[1][0]])
                else:
                    buttonPress([0, 2, button[0][2]])
        elif nbcoup==6:
            if game[2][2] == 2 and game[2][0] == 2:
                if game[1][0]==0:
                    buttonPress([1, 0, button[1][0]])
                elif game[2][1]==0:
                    buttonPress([2, 1, button[2][1]])

            elif game[2][2] == 2 and game[0][2] == 2:
                if game[0][1]==0:
                    buttonPress([0, 1, button[0][1]])
                else:
                    buttonPress([1, 2, button[1][2]])
            elif game[0][2]==2:
                if game[1][1]==0:
                    buttonPress([1, 1, button[1][1]])
                else:
                    buttonPress([0, 1, button[0][1]])

    #IA difficile
    if r.get()==3:
        if nbcoup==0:
            buttonPress([0, 0, button[0][0]])
        elif nbcoup==2:
            if game[2][2]==0:
                buttonPress([2, 2, button[2][2]])
            else:
                buttonPress([2, 0, button[2][0]])
        elif nbcoup==4:
            if game[1][1]==1 and (game[0][1]==1 or game[1][0]==1 or game[1][2]==1 or game[2][1]==1):
                if game[0][1]==1:
                    buttonPress([2, 1, button[2][1]])
                    egaliter = 1
                elif game[1][0] == 1:
                    buttonPress([1, 2, button[1][2]])
                    egaliter = 2
                elif game[1][2] == 1:
                    buttonPress([1, 0, button[1][0]])
                    egaliter = 3
                elif game[2][1] == 1:
                    buttonPress([0, 1, button[0][1]])
                    egaliter = 4

            elif game[2][2] == 2:
                if game[1][1]==0:
                    buttonPress([1, 1, button[1][1]])
                elif game[2][0] == 0:
                    buttonPress([2, 0, button[2][0]])
                else:
                    buttonPress([0, 2, button[0][2]])
            else:
                if game[1][0]==0:
                    buttonPress([1, 0, button[1][0]])
                else:
                    buttonPress([0, 2, button[0][2]])
        elif nbcoup==6:

            if game[2][2] == 2 and game[2][0] == 2:
                if game[1][0]==0:
                    buttonPress([1, 0, button[1][0]])
                elif game[2][1]==0:
                    buttonPress([2, 1, button[2][1]])

            elif game[2][2] == 2 and game[0][2] == 2:
                if game[0][1]==0:
                    buttonPress([0, 1, button[0][1]])
                else:
                    buttonPress([1, 2, button[1][2]])

            elif game[0][2]==2:

                if game[1][1]==0:
                    buttonPress([1, 1, button[1][1]])
                else:
                    buttonPress([0, 1, button[0][1]])
            else:
                if (egaliter==1 or egaliter==3) and game[2][0]==0:
                    buttonPress([2,0,button[2][0]])
                elif (egaliter==2 or egaliter==4) and game[0][2]==0:
                    buttonPress([0,2,button[0][2]])


                elif [game[0][2],game[1][1]]==[1,1] or [game[2][0],game[1][1]]==[1,1]:
                    if [game[0][2],game[1][1]]==[1,1]:
                        buttonPress([2, 0, button[2][0]])
                    else:
                        buttonPress([0, 2, button[0][2]])

                else:
                    x = posL[random.randint(0, len(posL) - 1)]
                    buttonPress([x[0], x[1], button[x[0]][x[1]]])
        else:
            x = posL[random.randint(0, len(posL) - 1)]
            buttonPress([x[0], x[1], button[x[0]][x[1]]])

def verifieRep(reponce):
    if reponce == True:
        newgame()
    else:
        quit()

#fonction verifie si le joueur peux jouer a cette case et change l'image du bouton
def buttonPress(button):
    global playing, nbcoup
    if game[button[0]][button[1]] == 0:
        game[button[0]][button[1]] = playing
        if playing == 1:
            button[2]['image'] = croix
            playing = 2
        else:
            button[2]['image'] = rond
            playing = 1
        nbcoup += 1
        statut = verifyGagnant()

        if statut == 1:
            verifieRep(messagebox.askretrycancel('','Bravo tu a gagné veux tu réessayer?',icon = 'info'))
        elif statut == 2:
            verifieRep(messagebox.askretrycancel('','le bot a gagné veux tu réessayer?',icon = 'info'))
        elif statut == 0:
            verifieRep(messagebox.askretrycancel('', 'Egalité veux tu réessayer?',icon = 'info'))

        else:
            if playing ==2:
                playbot()
            else:
                pass

    else:
        messagebox.showwarning("Erreur", "Tu ne peux pas jouer ici")
        print(game)

#fonction qui verifie si il y a une egaliter/ une victoire
def verifyGagnant():
    for i in range(3):
        if game[i] == [1, 1, 1] or [game[0][i], game[1][i], game[2][i]] == [1, 1, 1]:  # vertical/horizonal joueur 1
            return 1
        elif game[i] == [2, 2, 2] or [game[0][i], game[1][i], game[2][i]] == [2, 2, 2]:  # vertical/horizonal joueur 2
            return 2
    if [game[0][0], game[1][1], game[2][2]] == [1, 1, 1] or [game[2][0], game[1][1], game[0][2]] == [1, 1, 1]:  # diagonal joueur 1
        return 1
    if [game[0][0], game[1][1], game[2][2]] == [2, 2, 2] or [game[2][0], game[1][1], game[0][2]] == [2, 2, 2]:  # diagonal joueur 2
        return 2
    if nbcoup == 9:  # verifie si il a égalité
        return 0

#création des barres
barre = Canvas(root, width=530, height=20, bg='black', highlightbackground="black")
barre2 = Canvas(root, width=530, height=20, bg='black', highlightbackground="black")
barre3 = Canvas(root, width=20, height=530, bg='black', highlightbackground="black")
barre4 = Canvas(root, width=20, height=530, bg='black', highlightbackground="black")
barreBas = Canvas(root, width=530, height=70, bg='black', highlightbackground="black")

#création des boutons
button1 = Button(root, text="", image=rien, command=lambda: buttonPress([0, 0, button1]), width=160, height=160,border=False)
button2 = Button(root, text="", image=rien, command=lambda: buttonPress([0, 1, button2]), width=160, height=160,border=False)
button3 = Button(root, text="", image=rien, command=lambda: buttonPress([0, 2, button3]), width=160, height=160,border=False)
button4 = Button(root, text="", image=rien, command=lambda: buttonPress([1, 0, button4]), width=160, height=160,border=False)
button5 = Button(root, text="", image=rien, command=lambda: buttonPress([1, 1, button5]), width=160, height=160,border=False)
button6 = Button(root, text="", image=rien, command=lambda: buttonPress([1, 2, button6]), width=160, height=160,border=False)
button7 = Button(root, text="", image=rien, command=lambda: buttonPress([2, 0, button7]), width=160, height=160,border=False)
button8 = Button(root, text="", image=rien, command=lambda: buttonPress([2, 1, button8]), width=160, height=160,border=False)
button9 = Button(root, text="", image=rien, command=lambda: buttonPress([2, 2, button9]), width=160, height=160,border=False)
restartButton = Button(root, text='  restart  ', bg='white', command=newgame)
quitbutton = Button(root,text='   quit    ',bg='white',command=quit)

button = [[button1,button2,button3],
          [button4,button5,button6],
          [button7,button8,button9]]


Radiobutton(root,text= ' facile  ',variable=r,value=1,command=newgame).place(x=230,y=555)
Radiobutton(root,text=' moyen ',variable=r,value=2,command=newgame).place(x=330,y=555)
Radiobutton(root,text='difficile',variable=r,value=3,command=newgame).place(x=430,y=555)

#placement des barres et des boutons
barre3.grid(column=1, row=0, rowspan=5)
barre4.grid(column=3, row=0, rowspan=5)
button1.grid(column=0, row=0)
button2.grid(column=2, row=0)
button3.grid(column=4, row=0)
barre.grid(column=0, row=1, columnspan=5)
button4.grid(column=0, row=2)
button5.grid(column=2, row=2)
button6.grid(column=4, row=2)
barre2.grid(column=0, row=3, columnspan=5)
button7.grid(column=0, row=4)
button8.grid(column=2, row=4)
button9.grid(column=4, row=4)
barreBas.grid(column=0, row=5, columnspan=5)
restartButton.place(x=40, y=555)
quitbutton.place(x=140,y=555)


#boucle
root.mainloop()
