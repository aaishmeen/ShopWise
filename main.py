import json
import os
from datetime import datetime

FILE_PATH= "search_history.json"

def load_history():
    
    if not os.path.exists(FILE_PATH):
        return []
    
    with open (FILE_PATH,"r") as file:
        return json.load(file)

def save_history():
    with open(FILE_PATH,"w") as file:
        json.dump(search_history,file,indent=4)

def search_product():
    pass

def view_history():
    pass

def menu():
    print("1. Search Product ")
    print("2. View History ")
    print("3. Exit ")

search_history = load_history()

while True:
    print ( '-' * 35 )
    print("Welcome to ShopWise!")
    print ( '-' * 35 )

    menu()
    
    choice = input("Enter your Choice (1-3) : ")
    
    match choice :
        
        case "1" :
            search_product()

        case "2" :
            view_history()

        case "3" :
            print("Exiting Now !")
            print("Thank you for choosing ShopWise !")
            break       

        case _:
            print("Kindly Enter a Valid Choice") 
            


