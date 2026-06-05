import json
import os

FILE_PATH= os.path.join(
    os.path.dirname(__file__),
    "search_history.json"
)

def load_history():
    
    if not os.path.exists(FILE_PATH):
        return []
    
    with open (FILE_PATH,"r") as file:
        return json.load(file)

def save_history(search_history):
    with open(FILE_PATH,"w") as file:
        json.dump(search_history,file,indent=4)
