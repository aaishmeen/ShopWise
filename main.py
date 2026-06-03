import json
import os
from datetime import datetime

FILE_PATH= os.path.join(
    os.path.dirname(__file__),
    "search_history.json"
)

def load_history():
    
    if not os.path.exists(FILE_PATH):
        return []
    
    with open (FILE_PATH,"r") as file:
        return json.load(file)

def save_history():
    with open(FILE_PATH,"w") as file:
        json.dump(search_history,file,indent=4)

def pause():
    input("\nPress Enter To Continue......")

def search_product():
    
    product_name = input("Enter Product Name: ").strip()

    if not product_name:
       print("Product name cannot be empty! ")
       return
    
    current_time = datetime.now()

    date = current_time.strftime("%Y-%m-%d")
    time =  current_time.strftime("%H:%M:%S")

    search = {
        "product_name": product_name,
        "date": date,
        "time":time
    }

    search_history.append(search)

    save_history()

    print("Search saved successfully!")
    pause()


def view_history():

    if not search_history :
        print("No Search history Found !")
        pause()
        return

       
    print('-' * 65)
    print(f"{'No.':<5} {'Product Name':<25} {'Date':<15} {'Time':<10}")
    print('-' * 65)

    for index , search in enumerate(search_history,start=1):
        print(
            f"{index:<5}"
            f"{search['product_name']:<25}"
            f"{search['date']:<15}"
            f"{search['time']:<10}" 
                )
        
    print("-" * 65)    
    pause()

def delete_search_history():

    if not search_history:
        print("No Search History Found !")
        pause()
        return
    
    print('-' * 65)
    print(f"{'No.':<5} {'Product Name':<25} {'Date':<15} {'Time':<10}")
    print('-' * 65)

    for index , search in enumerate(search_history,start=1):
        print(f"{index}. {search['product_name']}")
        
    print("-" * 65)  

    delete_index= int(input("Enter Search History to Delete : "))

    search_history.pop(delete_index - 1 )

    save_history()
    
    print("Search History Deleted Successfully!")
    pause()



def menu():
    print("1. Search Product ")
    print("2. View History ")
    print("3. Delete Search History ")
    print("4. Exit ")

search_history = load_history()

while True:
    print ( '-' * 35 )
    print("Welcome to ShopWise!")
    print ( '-' * 35 )

    menu()
    
    choice = input("Enter your Choice (1-4) : ")
    
    match choice :
        
        case "1" :
            search_product()

        case "2" :
            view_history()

        case "3":
            delete_search_history()    

        case "4" :
            print("Exiting Now !")
            print("Thank you for choosing ShopWise !")
            break       

        case _:
            print("Kindly Enter a Valid Choice") 
            


