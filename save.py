import json

# Initialisation des variables de sauvegarde
data_secret = ""
data_focus = ""
data_selector = ""

data_line1 = ""
data_line2 = ""
data_line3 = ""
data_line4 = ""
data_line5 = ""
data_line6 = ""
data_line7 = ""
data_line8 = ""
data_line9 = ""
data_line10 = ""

data_pegs1 = ""
data_pegs2 = ""
data_pegs3 = ""
data_pegs4 = ""
data_pegs5 = ""
data_pegs6 = ""
data_pegs7 = ""
data_pegs8 = ""
data_pegs9 = ""
data_pegs10 = ""

# fonction de remplissage du template de la sauvegarde avec les valeurs courantes du jeu
def createSave():
    jsonData = {
        "secret": data_secret,
        "focus": data_focus,
        "selector": data_selector,
        "line1": int(data_line1),
        "line2": int(data_line2),
        "line3": int(data_line3),
        "line4": int(data_line4),
        "line5": int(data_line5),
        "line6": int(data_line6),
        "line7": int(data_line7),
        "line8": int(data_line8),
        "line9": int(data_line9),
        "line10": int(data_line10),
        "pegs1": data_pegs1,
        "pegs2": data_pegs2,
        "pegs3": data_pegs3,
        "pegs4": data_pegs4,
        "pegs5": data_pegs5,
        "pegs6": data_pegs6,
        "pegs7": data_pegs7,
        "pegs8": data_pegs8,
        "pegs9": data_pegs9,
        "pegs10": data_pegs10
    }
    
    # On converti notre dic en objet json puis on le return
    return json.dumps(jsonData)

# Fonction de lecture du fichier de sauvegarde et de remplissage des variables pour les attribuer au jeu
def loadSave(link):
    global data_secret, data_focus, data_selector
    global data_line1, data_line2, data_line3, data_line4, data_line5, data_line6, data_line7, data_line8, data_line9, data_line10
    global data_pegs1, data_pegs2, data_pegs3, data_pegs4, data_pegs5, data_pegs6, data_pegs7, data_pegs8, data_pegs9, data_pegs10
    
    saveFile = open(link, "r")
    dataFile = saveFile.read()
    jsonTxt = json.loads(dataFile)
    
    data_secret = jsonTxt["secret"]
    data_focus = jsonTxt["focus"]
    data_selector = jsonTxt["selector"]
    
    data_line1 = jsonTxt["line1"]
    data_line2 = jsonTxt["line2"]
    data_line3 = jsonTxt["line3"]
    data_line4 = jsonTxt["line4"]
    data_line5 = jsonTxt["line5"]
    data_line6 = jsonTxt["line6"]
    data_line7 = jsonTxt["line7"]
    data_line8 = jsonTxt["line8"]
    data_line9 = jsonTxt["line9"]
    data_line10 = jsonTxt["line10"]
    
    data_pegs1 = jsonTxt["pegs1"]
    data_pegs2 = jsonTxt["pegs2"]
    data_pegs3 = jsonTxt["pegs3"]
    data_pegs4 = jsonTxt["pegs4"]
    data_pegs5 = jsonTxt["pegs5"]
    data_pegs6 = jsonTxt["pegs6"]
    data_pegs7 = jsonTxt["pegs7"]
    data_pegs8 = jsonTxt["pegs8"]
    data_pegs9 = jsonTxt["pegs9"]
    data_pegs10 = jsonTxt["pegs10"]
    
    saveFile.close()
    
    return True
