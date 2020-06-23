import save as save
from tkinter import * 
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk # A installer avec PIP
from random import *
import os
import sys
import socket
import requests # A installer avec PIP
import webbrowser

#################  API KEY  #################
############## NE PAS MODIFIER ##############
apiKey = "rk9634p38o3v5sro94yr"
#############################################
#############################################
  
# Variable contanant la combinaison secrète    
findCode = ""
    
# Ligne et position du pion actuel    
line = 1
position = 1
selectorY = 655

# Partie issue ou non d'une sauvegarde
backupPart = False

# Initialisation des tableaux de données pour chaques lignes et pour les picos
line1 = [0, 0, 0, 0]
line2 = [0, 0, 0, 0]
line3 = [0, 0, 0, 0]
line4 = [0, 0, 0, 0]
line5 = [0, 0, 0, 0]
line6 = [0, 0, 0, 0]
line7 = [0, 0, 0, 0]
line8 = [0, 0, 0, 0]
line9 = [0, 0, 0, 0]
line10 = [0, 0, 0, 0]
lineResult = [0, 0, 0, 0]
pegsSave = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Stockage des pions ajouté pour chaque bouton (optionel mais toujours bien utile)
btnColorRegister = [0, 0, 0, 0, 0, 0]

lineTab = line1

# fonction permettant de générer une combinaison secrète aléatoirement
def randomFindCode():
    global findCode
    findCode = ""
    for i in range(4):
        findCode += str(randint(1, 6))
        
randomFindCode()

# Objet Pion
class Pawn:
    
    def __init__(self, line, position, color, label):
        self.line = line
        self.position = position
        self.color = color
        self.label = label
        
        if color == 1: self.label = Label(frame, image=colorBlueImg, border=0)
        elif color == 2: self.label = Label(frame, image=colorGreenImg, border=0)
        elif color == 3: self.label = Label(frame, image=colorOrangeImg, border=0)
        elif color == 4: self.label = Label(frame, image=colorPinkImg, border=0)
        elif color == 5: self.label = Label(frame, image=colorRedImg, border=0)
        elif color == 6: self.label = Label(frame, image=colorYellowImg, border=0)
        
        self.label.place(x=45 + (54*position) - (position-1), y=selectorY-8)
        
        
    def destroy(self):
        self.label.destroy()
        
    def getLine(self):
        return self.line
    
    def getPosition(self):
        return self.position
    
    def getColor(self):
        return self.color
    
# Objet placement des pions après vérification du résultat    
class ResultPawn:
        
    def __init__(self, posX, posY, color, label):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.label = label
        
        if color == 1: self.label = Label(frame, image=colorBlueImg, border=0)
        elif color == 2: self.label = Label(frame, image=colorGreenImg, border=0)
        elif color == 3: self.label = Label(frame, image=colorOrangeImg, border=0)
        elif color == 4: self.label = Label(frame, image=colorPinkImg, border=0)
        elif color == 5: self.label = Label(frame, image=colorRedImg, border=0)
        elif color == 6: self.label = Label(frame, image=colorYellowImg, border=0)
        
        self.label.place(x=self.posX, y=self.posY)
        
    def destroy(self):
        self.label.destroy()
    
# Objet pegs        
class Pegs:
    
    def __init__(self, line, pegsCode, label1, label2, label3, label4):
        self.line = line
        self.pegsCode = pegsCode
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        
        if line > 5:
            marging = 62
        else:
            marging = 61
        
        if pegsCode[0] == "1":
            self.label1 = Label(frame, image=colorPegsBlack, border=0)
            self.label1.place(x=320, y=650 - (marging * (line-1) ))
        elif pegsCode[0] == "2":
            self.label1 = Label(frame, image=colorPegsGreen, border=0)
            self.label1.place(x=320, y=650 - (marging * (line-1) ))
            
        if pegsCode[1] == "1":
            self.label2 = Label(frame, image=colorPegsBlack, border=0)
            self.label2.place(x=335, y=650 - (marging * (line-1) ))
        elif pegsCode[1] == "2":
            self.label2 = Label(frame, image=colorPegsGreen, border=0)
            self.label2.place(x=335, y=650 - (marging * (line-1) ))
            
        if pegsCode[2] == "1":
            self.label3 = Label(frame, image=colorPegsBlack, border=0)
            self.label3.place(x=335, y=665 - (marging * (line-1) ))
        elif pegsCode[2] == "2":
            self.label3 = Label(frame, image=colorPegsGreen, border=0)
            self.label3.place(x=335, y=665 - (marging * (line-1) ))
            
        if pegsCode[3] == "1":
            self.label4 = Label(frame, image=colorPegsBlack, border=0)
            self.label4.place(x=320, y=665 - (marging * (line-1) ))
        elif pegsCode[3] == "2":
            self.label4 = Label(frame, image=colorPegsGreen, border=0)
            self.label4.place(x=320, y=665 - (marging * (line-1) ))
            
            
    def pegsDestroy(self):
        if self.label1 != 0: self.label1.destroy()
        if self.label2 != 0: self.label2.destroy()
        if self.label3 != 0: self.label3.destroy()
        if self.label4 != 0: self.label4.destroy()
        
    def getPegsCode(self):
        return self.pegsCode    
    
# Fonction permettant de faire monter le curseur de ligne (curseur tout à gauche)
def moveUpSelector():
    global selectorY
    global line
    if line < 10: 
        label.place(x=15, y=selectorY-60)
        selectorY-=62
        line+=1
        
# Fonction permettant d'ajouter un pion sur le plateau        
def setPawn(color):
    global position
    global lineTab
    
    btnColorRegister[color-1] = btnColorRegister[color-1]+1
    
    if position < 5:
        lineTab[position-1] = Pawn(line, position, color, 0)
        position+=1
       
# Fonction permettant de récupérer le code couleur pour une ligne donnée    
def getLineColorCode(line):
    tempColor = "0"
    for i in range(4):
        if line == 1 and line1[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line1[i].getColor())
            save.data_line1 = tempColor
        if line == 2 and line2[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line2[i].getColor())
            save.data_line2 = tempColor
        if line == 3 and line3[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line3[i].getColor())
            save.data_line3 = tempColor
        if line == 4 and line4[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line4[i].getColor())
            save.data_line4 = tempColor
        if line == 5 and line5[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line5[i].getColor())
            save.data_line5 = tempColor
        if line == 6 and line6[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line6[i].getColor())
            save.data_line6 = tempColor
        if line == 7 and line7[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line7[i].getColor())
            save.data_line7 = tempColor
        if line == 8 and line8[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line8[i].getColor())
            save.data_line8 = tempColor
        if line == 9 and line9[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line9[i].getColor())
            save.data_line9 = tempColor
        if line == 10 and line10[0] != 0: 
            if tempColor == "0": tempColor = ""
            tempColor += str(line10[i].getColor())
            save.data_line10 = tempColor
            
    return tempColor
        
# Fonction comparant la ligne validée avec la combinaison secrète + détecteur de victoire / défaite + référencement de la partie en ligne
def checkLine():
    global position
    
    lineCode = ""
    pegsCode = ""
    result = ""
    count = 0
    #identicalColor = "-"
    
    if position == 5:
        position = 1
        
        for i in range(len(lineTab)):
            lineCode += str(lineTab[i].getColor())
                
                
        postBlack = 0
        repeatLineColor = False
     
        # Comparaison et vérification entre la ligne et la combinaison secrète
        for index in lineCode:
            if findCode.count(index) == 0:
                pegsCode += str(0)
            else:
                if str(findCode)[count] == index:
                    pegsCode += str(2)
                else:
                    pegsCode += str(1)
                    postBlack += 1

            count+=1
         
        repeatLineColor = False
        for i in range(6):
            if btnColorRegister[i] > 3:
                repeatLineColor = True
                break    
            
                
        result = "".join(sorted(pegsCode))
        if repeatLineColor == True:
            result = result.replace("1", "0", postBlack)
        setLinePegs(result)
        
        for i in range(6):
            if btnColorRegister[i] != 0:
                btnColorRegister[i] = 0
        
        if result == "2222":
            setResultFindColor(0)
            
            if backupPart == False:
                try:
                    # Vérification de la connexion à internet
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect(("www.google.com", 80))
                    
                    # Enregistrement de la partie en ligne 
                    requests.get("https://mastermind.fr-fr.cc/api/setRank.php?apikey='"+apiKey+"'&line="+str(int(line))+"&secret="+findCode+"")
                    answer = messagebox.askyesno("Question","Vous remportez la partie !\nVotre partie à été référencé sur le site MasterMind-Rank \nSouhaitez-vous recommencer une nouvelle partie ?")
                except:
                    print("Aucune connexion a internet")
                    answer = messagebox.askyesno("Question","Vous remportez la partie !\nVotre partie n'a pas été référencé car vous n'êtes pas connecté à Internet !\nSouhaitez-vous recommencer une nouvelle partie ?")
                    
            else: 
                answer = messagebox.askyesno("Question","Vous remportez la partie !\nVotre partie n'a pas été référencé car elle provient d'une sauvegarde\nSouhaitez-vous recommencer une nouvelle partie ?")
            
            if answer == True:
                restartGame()
            else:
                sys.exit()
        else :
            if(line != 10):
                moveUpSelector()
                switchTabs()
            else:
                setResultFindColor(0)
                
                answer = messagebox.askyesno("Question","Game Over !\nSouhaitez-vous recommencer une nouvelle partie ?")
                if answer == True:
                    restartGame()
                else:
                    sys.exit()
        
        
 # Fonction permettant de relancer une nouvelle partie       
def restartGame():
    global line, position, selectorY, lineTab, pegsSave, backupPart
    
    randomFindCode()
    line = 0
    position = 1
    selectorY = 655+62
    
    for i in range(10):
        if i == 0: lineTab = line1
        elif i == 1: lineTab = line2
        elif i == 2: lineTab = line3
        elif i == 3: lineTab = line4
        elif i == 4: lineTab = line5
        elif i == 5: lineTab = line6
        elif i == 6: lineTab = line7
        elif i == 7: lineTab = line8
        elif i == 8: lineTab = line9
        elif i == 9: lineTab = line10
        
        for i in range(len(lineTab)):
            if lineTab[i] != 0: lineTab[i].destroy()
    
    lineTab = line1
    
    for i in range(10):
        if pegsSave[i] != 0: pegsSave[i].pegsDestroy()
        
    for i in range(4):
        if lineResult[i] != 0: lineResult[i].destroy()
    
    setResultFindColor(1)
    moveUpSelector()
    backupPart = False

    
# Fonction permettant d'ajouter les picos à la dernière ligne validée        
def setLinePegs(pegsCode):
    global pegsSave
    
    pegsSave[line-1] = Pegs(line, pegsCode, 0, 0, 0, 0)
    
# Fonction permettant d'afficher la combinaison secrète en cas de victoire ou de défaite
def setResultFindColor(action):   
    if action == 0:
        count = 0
        
        for index in findCode:
            lineResult[count] = ResultPawn(205 + (53*count), 724, int(index), 0)
            
            count +=1
        
# Fonction permettant de supprimer une ligne (bouton rouge)        
def clearLine():
    global position
    
    for i in range(6):
        if btnColorRegister[i] != 0:
            btnColorRegister[i] = 0
    
    for i in range(len(lineTab)):
        if lineTab[i] != 0: lineTab[i].destroy()
        
    position = 1
    
# Fonction permettant de changer le tableau de stockage de la ligne courante    
def switchTabs():
    global lineTab
    
    if line == 1: lineTab = line1
    elif line == 2: lineTab = line2
    elif line == 3: lineTab = line3
    elif line == 4: lineTab = line4
    elif line == 5: lineTab = line5
    elif line == 6: lineTab = line6
    elif line == 7: lineTab = line7
    elif line == 8: lineTab = line8
    elif line == 9: lineTab = line9
    elif line == 10: lineTab = line10

# Fonction permettant de proposer de sauvegarder ou de reprendre une partie
def saveManager():
    answer = messagebox.askyesno("Question","Souhaitez-vous sauvegarder cette partie ?")
    if answer == True:
        fileFrame = filedialog.asksaveasfile(mode='w', defaultextension=".json", initialdir="/", filetypes=(("Fichier JSON","*.json"),("Fichier JSON","*.json"))) 
        if fileFrame is None:
            print("Annulation de la sauvegarde ...")
        else:
            createAndApplySave(fileFrame)
    else:
        answer = messagebox.askyesno("Question","Souhaitez-vous charger une partie ?")
        if answer == True:
            fileFrame = filedialog.askopenfilename(initialdir="/", title="Sélectionnez votre sauvegarde", filetypes=(("Fichier JSON","*.json"),("Tous les fichiers","*.*")))
            if len(fileFrame) > 0: 
                restartGame()
                readAndApplySave(fileFrame)

# Fonction permettant de créer et d'enregistrer une sauvegarde
def createAndApplySave(fileFrame):
    save.data_secret = findCode
    save.data_focus = line
    save.data_selector = selectorY
    
    save.data_line1 = getLineColorCode(1)
    save.data_line2 = getLineColorCode(2)
    save.data_line3 = getLineColorCode(3)
    save.data_line4 = getLineColorCode(4)
    save.data_line5 = getLineColorCode(5)
    save.data_line6 = getLineColorCode(6)
    save.data_line7 = getLineColorCode(7)
    save.data_line8 = getLineColorCode(8)
    save.data_line9 = getLineColorCode(9)
    save.data_line10 = getLineColorCode(10)
    
    for i in range(len(pegsSave)):
        if i == 0 and pegsSave[i] != 0: save.data_pegs1 = pegsSave[i].getPegsCode()
        elif i == 1 and pegsSave[i] != 0: save.data_pegs2 = pegsSave[i].getPegsCode()
        elif i == 2 and pegsSave[i] != 0: save.data_pegs3 = pegsSave[i].getPegsCode()
        elif i == 3 and pegsSave[i] != 0: save.data_pegs4 = pegsSave[i].getPegsCode()
        elif i == 4 and pegsSave[i] != 0: save.data_pegs5 = pegsSave[i].getPegsCode()
        elif i == 5 and pegsSave[i] != 0: save.data_pegs6 = pegsSave[i].getPegsCode()
        elif i == 6 and pegsSave[i] != 0: save.data_pegs7 = pegsSave[i].getPegsCode()
        elif i == 7 and pegsSave[i] != 0: save.data_pegs8 = pegsSave[i].getPegsCode()
        elif i == 8 and pegsSave[i] != 0: save.data_pegs9 = pegsSave[i].getPegsCode()
        elif i == 9 and pegsSave[i] != 0: save.data_pegs10 = pegsSave[i].getPegsCode()
    
    fileFrame.write(save.createSave())
    fileFrame.close()
    
    messagebox.showinfo(title="Partie sauvegardée", message="Votre partie a bien été sauvegardée !")

# Fonction permettant de lire et d'appliquer une sauvegarde    
def readAndApplySave(link):
    global findCode, line, selectorY, position, backupPart, lineTab
    
    if save.loadSave(link) == True:
        
        findCode = str(save.data_secret)
        line = 1
        selectorY = 655
        lineTab = line1
        
        for i in range(int(save.data_focus)-1):
            for j in range(4):
                if line == 1: varConvert = "" + str(save.data_line1)
                elif line == 2: varConvert = "" + str(save.data_line2)
                elif line == 3: varConvert = "" + str(save.data_line3)
                elif line == 4: varConvert = "" + str(save.data_line4)
                elif line == 5: varConvert = "" + str(save.data_line5)
                elif line == 6: varConvert = "" + str(save.data_line6)
                elif line == 7: varConvert = "" + str(save.data_line7)
                elif line == 8: varConvert = "" + str(save.data_line8)
                elif line == 9: varConvert = "" + str(save.data_line9)
                elif line == 10: varConvert = "" + str(save.data_line10)
                
                setPawn(int(varConvert[j]))
                
            position = 1
            
            if line == 1: setLinePegs(save.data_pegs1)
            elif line == 2: setLinePegs(save.data_pegs2)
            elif line == 3: setLinePegs(save.data_pegs3)
            elif line == 4: setLinePegs(save.data_pegs4)
            elif line == 5: setLinePegs(save.data_pegs5)
            elif line == 6: setLinePegs(save.data_pegs6)
            elif line == 7: setLinePegs(save.data_pegs7)
            elif line == 8: setLinePegs(save.data_pegs8)
            elif line == 9: setLinePegs(save.data_pegs9)
            elif line == 10: setLinePegs(save.data_pegs10)
            
            moveUpSelector()
            switchTabs()
        
        backupPart = True
        print("Save ready to play !")
    else:
        print("Invalid save file !")
      
# Fonction permettant d'ouvrir le site de classement sur le navigateur par defaut        
def openRankPage():
    webbrowser.open('https://mastermind.fr-fr.cc/')
    
# Création et paramètrage de la fenêtre    
frame = Tk()
frame.resizable(width=False, height=False)
frame.title("MasterMind v1.2.5 | 1PYTH")

# Création du canvas
canvas = Canvas(frame, width=422, height=788, background="white")

imgBG = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/plate.png") 
background_label = Label(frame, image=imgBG) 
background_label.place(x=0, y=0, relwidth=1, relheight=1)

imgSelector = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/line_selector.png") 
label = Label(frame, image=imgSelector, border=0)
label.place(x=15, y=selectorY)

# On définie toutes les images utiles au jeu
btnValidImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/valid_btn.png")
btnCancelImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/cancel_btn.png")
btnSaveImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/save_btn.png")
btnRankImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/rank.png")

colorBlueImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/blue_color.png") 
colorGreenImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/green_color.png") 
colorOrangeImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/orange_color.png") 
colorPinkImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/pink_color.png") 
colorRedImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/red_color.png") 
colorYellowImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/yellow_color.png") 

# Et on créer tous nos boutons
colorPegsBlack = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/pegs_black.png") 
colorPegsGreen = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/pegs_green.png") 

btnValid = Button(frame, background='white', image=btnValidImg, border=0, cursor="hand2", command = checkLine)
btnValid = canvas.create_window(391, 514, window=btnValid)

btnCancel = Button(frame, background='white', image=btnCancelImg, border=0, cursor="hand2", command = clearLine)
btnCancel = canvas.create_window(391, 600, window=btnCancel)

btnSave = Button(frame, background='white', image=btnSaveImg, border=0, cursor="hand2", command = saveManager)
btnSave = canvas.create_window(391, 660, window=btnSave)

btnRank = Button(frame, background='white', image=btnRankImg, border=0, cursor="hand2", command = openRankPage)
btnRank = canvas.create_window(391, 40, window=btnRank)

btnBlue = Button(frame, background='white', image=colorBlueImg, border=0, cursor="hand2", command= lambda x=1:setPawn(x))
btnBlue = canvas.create_window(391, 105, window=btnBlue)

btnGreen = Button(frame, background='white', image=colorGreenImg, border=0, cursor="hand2", command= lambda x=2:setPawn(x))
btnGreen = canvas.create_window(391, 167, window=btnGreen)

btnOrange = Button(frame, background='white', image=colorOrangeImg, border=0, cursor="hand2", command= lambda x=3:setPawn(x))
btnOrange = canvas.create_window(391, 229, window=btnOrange)

btnPink = Button(frame, background='white', image=colorPinkImg, border=0, cursor="hand2", command= lambda x=4:setPawn(x))
btnPink = canvas.create_window(391, 291, window=btnPink)

btnRed = Button(frame, background='white', image=colorRedImg, border=0, cursor="hand2", command= lambda x=5:setPawn(x))
btnRed = canvas.create_window(391, 353, window=btnRed)

btnYellow = Button(frame, background='white', image=colorYellowImg, border=0, cursor="hand2", command= lambda x=6:setPawn(x))
btnYellow = canvas.create_window(391, 415, window=btnYellow)

canvas.pack()
frame.mainloop()


#
# Ceci est un commentaire jugé inutile par la FFCP (Fédération Française des Commentaires en Python)
#