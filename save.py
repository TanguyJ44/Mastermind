import json
import os

def loadSave():
    mon_fichier = open(os.path.dirname(__file__)+"\save.json", "r")
    contenu = mon_fichier.read()
    jsonTxt = json.loads(contenu)
    
    print(jsonTxt["secret"])
    
    mon_fichier.close()
