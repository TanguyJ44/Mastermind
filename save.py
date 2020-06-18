import json

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
