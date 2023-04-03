from tkinter import *
from random import *

def clavier(event) :
    global ecran
    global canvas
    global sens
    global point
    global positions
    global a
    global vitesse
    global record
    global pause
    touche = event.keysym
    if touche == "Return" :
        if ecran == 1 :
            ecran = 2
            canvas.delete('all')
            non = 1
            while non == 1 :
                a = randint(0,19)
                b = randint(0,19)
                if a < 10 :
                    a = "0"+str(a)
                else :
                    a = str(a)
                if b < 10 :
                    b = "0"+str(b)
                else :
                    b = str(b)
                point = a+"/"+b
                non = 0
                for i in range (len(positions)) :
                    if point == positions[i] :
                        non = 1
            a = 0
            vitesse = 501
            pause = 0
            creation()
            jeu()
        elif ecran == 2 :
            if pause == 0 :
                pause = 1
            else :
                pause = 0
                jeu()
        elif ecran == 3 :
            canvas.delete('all')
            ecran = 1
            if len(positions) > record :
                record = len(positions)-2
            debut()
    elif ecran == 2 and a == 0 :
        if touche == "Up" and not sens == 3 :
            sens = 1
            a = 1
        elif touche == "Down" and not sens == 1 :
            sens = 3
            a = 1
        elif touche == "Left" and not sens == 2 :
            sens = 4
            a = 1
        elif touche == "Right" and not sens == 4 :
            sens = 2
            a = 1

def gameover() :
    global canvas
    global ecran
    ecran = 3
    texte = canvas.create_text(250,250,text="GAME OVER",font="Serif 28",fill='red')

def creation() :
    global canvas
    global positions
    global point
    canvas.delete('all')
    for i in range (len(positions)-1) :
        x = int(positions[i][0])*10+int(positions[i][1])
        y = int(positions[i][3])*10+int(positions[i][4])
        rec = canvas.create_rectangle(1+x*25,1+y*25,24+x*25,24+y*25,fill='white')
    x = int(positions[len(positions)-1][0])*10+int(positions[len(positions)-1][1])
    y = int(positions[len(positions)-1][3])*10+int(positions[len(positions)-1][4])
    rec = canvas.create_rectangle(1+x*25,1+y*25,24+x*25,24+y*25,fill='black')
    x = int(point[0])*10+int(point[1])
    y = int(point[3])*10+int(point[4])
    rec = canvas.create_rectangle(5+x*25,5+y*25,20+x*25,20+y*25,fill='red')

def jeu() :
    global positions
    global point
    global a
    global scoreboard
    global vitesse
    global pause
    if pause == 0 :
        if sens == 1 :
            x = positions[len(positions)-1][0]+positions[len(positions)-1][1]
            y = (int(positions[len(positions)-1][3])*10+int(positions[len(positions)-1][4]))-1
            if y == -1 :
                y = "19"
            elif y < 10 :
                y = "0"+str(y)
            else :
                y = str(y)
            positions += [x+"/"+y]
        elif sens == 3 :
            x = positions[len(positions)-1][0]+positions[len(positions)-1][1]
            y = (int(positions[len(positions)-1][3])*10+int(positions[len(positions)-1][4]))+1
            if y == 20 :
                y = "00"
            elif y < 10 :
                y = "0"+str(y)
            else :
                y = str(y)
            positions += [x+"/"+y]
        elif sens == 4 :
            x = (int(positions[len(positions)-1][0])*10+int(positions[len(positions)-1][1]))-1
            y = positions[len(positions)-1][3]+positions[len(positions)-1][4]
            if x == -1 :
                x = "19"
            elif x < 10 :
                x = "0"+str(x)
            else :
                x = str(x)
            positions += [x+"/"+y]
        elif sens == 2 :
            x = (int(positions[len(positions)-1][0])*10+int(positions[len(positions)-1][1]))+1
            y = positions[len(positions)-1][3]+positions[len(positions)-1][4]
            if x == 20 :
                x = "00"
            elif x < 10 :
                x = "0"+str(x)
            else :
                x = str(x)
            positions += [x+"/"+y]

        if positions[len(positions)-1] == point :
                non = 1
                while non == 1 :
                    a = randint(0,19)
                    b = randint(0,19)
                    if a < 10 :
                        a = "0"+str(a)
                    else :
                        a = str(a)
                    if b < 10 :
                        b = "0"+str(b)
                    else :
                        b = str(b)
                    point = a+"/"+b
                    non = 0
                    for i in range (len(positions)) :
                        if point == positions[i] :
                            non = 1
        else :
            del positions[0:1]
        scoreboard.delete('all')
        texte = scoreboard.create_text(45,20,text="score : ",font="Serif 16")
        texte = scoreboard.create_text(90,21,text=len(positions)-2,font="Serif 16")
        texte = scoreboard.create_text(430,20,text="record : ",font="Serif 16")
        texte = scoreboard.create_text(480,21,text=record,font="Serif 16")
        if vitesse > 200 :
            vitesse -= 1
        decode = 0
        non = 0
        while decode < len(positions)-1 and non == 0 :
            if positions[len(positions)-1] == positions[decode] :
                non = 1
            decode += 1
        if non == 1 :
            gameover()
        else :
            creation()
            a = 0
            canvas.after(vitesse,jeu)

def debut() :
    global ecran
    global sens
    global positions
    global canvas
    global record
    ecran = 1
    sens = 2
    positions = ["09/09","10/09"]
    texte = canvas.create_text(250,250,text="Appuyer sur entrée pour commencer.",font="Serif 16")
    scoreboard.delete('all')
    texte = scoreboard.create_text(45,20,text="score : ",font="Serif 16")
    texte = scoreboard.create_text(90,21,text="0",font="Serif 16")
    texte = scoreboard.create_text(430,20,text="record : ",font="Serif 16")
    texte = scoreboard.create_text(480,21,text=record,font="Serif 16")

fenetre = Tk()
fenetre.title("Snake")

scoreboard = Canvas(fenetre,width=500,height=40,bg='grey')
scoreboard.pack()
canvas = Canvas(fenetre,width=500,height=500,bg='white')
canvas.pack()

record = 0
debut()

canvas.focus_set()
canvas.bind("<Key>",clavier)

fenetre.mainloop()