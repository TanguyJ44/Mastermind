from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
from random import *
import os
import sys
    
findCode = ""
    
line = 1
position = 1
selectorY = 655

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

lineTab = line1

def randomFindCode():
    global findCode
    findCode = ""
    for i in range(4):
        findCode += str(randint(1, 4))
        
randomFindCode()


class Pawn:
    
    def __init__(self, line, position, color, label):
        self.line = line
        self.position = position
        self.color = color
        
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
    

def moveUpSelector():
    global selectorY
    global line
    if line < 10: 
        label.place(x=15, y=selectorY-60)
        selectorY-=62
        line+=1
        
        
def setPawn(color):
    global position
    global lineTab
    
    if position < 5:
        lineTab[position-1] = Pawn(line, position, color, 0)
        position+=1
        

def checkLine():
    global position
    
    lineCode = ""
    pegsCode = ""
    result = ""
    count = 0
    
    if position == 5:
        position = 1
        
        for i in range(len(lineTab)):
            lineCode += str(lineTab[i].getColor())
        
        for index in lineCode:
            if findCode.count(index) == 0:
                pegsCode += str(0)
            else :
                if str(findCode)[count] != index:
                    pegsCode += str(1)
                else:
                    pegsCode += str(2)
                
            count+=1
                
        result = "".join(sorted(pegsCode))
        #print(result)
        setLinePegs(result)
        
        if result == "2222":
            setResultFindColor(0)
            
            answer = messagebox.askyesno("Question","Vous remportez la partie !\nSouhaitez-vous recommencer une nouvelle partie ?")
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
        
        
        
def restartGame():
    global line 
    global position
    global selectorY
    global lineTab
    global pegsSave
    
    randomFindCode()
    line = 0
    position = 1
    selectorY = 655+62
    
    for i in range(10):
        if i == 0: lineTab = line1
        elif i == 1: lineTab = line1
        elif i == 2: lineTab = line2
        elif i == 3: lineTab = line3
        elif i == 4: lineTab = line4
        elif i == 5: lineTab = line5
        elif i == 6: lineTab = line6
        elif i == 7: lineTab = line7
        elif i == 8: lineTab = line8
        elif i == 9: lineTab = line9
        
        for i in range(len(lineTab)):
            if lineTab[i] != 0: lineTab[i].destroy()
    
    lineTab = line1
    
    for i in range(10):
        if pegsSave[i] != 0: pegsSave[i].pegsDestroy()
        
    for i in range(4):
        lineResult[i].destroy()
    
    setResultFindColor(1)
    
    moveUpSelector()
    
        
def setLinePegs(pegsCode):
    global pegsSave
    
    pegsSave[line] = Pegs(line, pegsCode, 0, 0, 0, 0)
    

def setResultFindColor(action):   
    if action == 0:
        count = 0
        
        for index in findCode:
            lineResult[count] = ResultPawn(205 + (53*count), 724, int(index), 0)
            
            count +=1
        
        
def clearLine():
    global position
    
    for i in range(len(lineTab)):
        if lineTab[i] != 0: lineTab[i].destroy()
        
    position = 1
    
    
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
    
    
frame = Tk()
frame.resizable(width=False, height=False)
frame.title("MasterMind v1.2.5 | 1PYTH")

canvas = Canvas(frame, width=422, height=788, background="white")

imgBG = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/plate.png") 
background_label = Label(frame, image=imgBG) 
background_label.place(x=0, y=0, relwidth=1, relheight=1)

imgSelector = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/line_selector.png") 
label = Label(frame, image=imgSelector, border=0)
label.place(x=15, y=selectorY)


btnValidImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/valid_btn.png")
btnCancelImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/cancel_btn.png")
btnSaveImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/save_btn.png")

colorBlueImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/blue_color.png") 
colorGreenImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/green_color.png") 
colorOrangeImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/orange_color.png") 
colorPinkImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/pink_color.png") 
colorRedImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/red_color.png") 
colorYellowImg = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/yellow_color.png") 

colorPegsBlack = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/pegs_black.png") 
colorPegsGreen = PhotoImage(file = os.path.dirname( __file__ )+"/imgs/pegs_green.png") 

btnValid = Button(frame, background='white', image=btnValidImg, border=0, cursor="hand2", command = checkLine)
btnValid = canvas.create_window(391, 514, window=btnValid)

btnCancel = Button(frame, background='white', image=btnCancelImg, border=0, cursor="hand2", command = clearLine)
btnCancel = canvas.create_window(391, 600, window=btnCancel)

btnSave = Button(frame, background='white', image=btnSaveImg, border=0, cursor="hand2")
btnSave = canvas.create_window(391, 660, window=btnSave)

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
