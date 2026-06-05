from utils import pause
from api_handler import get_products
from storage import load_history, save_history
from datetime import datetime

def search_product():
    
    product_name = input("Enter Product Name: ").strip()

    if not product_name:
      print("Product name cannot be empty!")
      pause()
      return 
    
    data = get_products(product_name)

    products = data["products"]

    if not products:
        print("No products found.")
        pause()
        return

    print(f"\nProducts Found: {len(products)}")
    print("-" * 50)
    print(f"\nSearch Results for: {product_name}")
    print("-" * 50)

    for index, product in enumerate(products, start=1):
        print(f"{index}. {product['title']}")
        print(f"   Category : {product['category']}")
        print(f"   Price : ${product['price']}")
        print("-" * 50)

    current_time = datetime.now()

    date = current_time.strftime("%Y-%m-%d")
    time =  current_time.strftime("%H:%M:%S")

    search = {
        "product_name": product_name,
        "date": date,
        "time":time
    }

    search_history.append(search)

    save_history(search_history)

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
    try :
      delete_index= int(input("Enter Search History to Delete : "))
    except ValueError:
        print("Invalid Input") 
        pause()
        return

    if delete_index < 1 or delete_index > len(search_history):
        print("Invalid Operation !")
        pause()
        return

    search_history.pop(delete_index - 1 )

    save_history(search_history)
    
    print("Search History Deleted Successfully!")
    pause()

def clear_search_history():
    if not search_history:
        print("No Search History Found !")
        pause()
        return 
    
    confirm_del = input("Are you sure you want to clear all search history? (y/n) : ").lower()

    if confirm_del == 'y':
        search_history.clear()
        save_history(search_history)
        print("Search History Cleared Successfully !")

    else:
        print("Operation Cancelled !")
        
    pause()    

def menu():
    print("1. Search Product ")
    print("2. View History ")
    print("3. Delete Search History ")
    print("4. Clear Search History ")
    print("5. Exit ")

search_history = load_history()

while True:

    print ( '-' * 35 )
    print("Welcome to ShopWise!")
    print ( '-' * 35 )

    menu()
    
    choice = input("Enter your Choice (1-5) : ")
    
    match choice :
        
        case "1" :
            search_product()

        case "2" :
            view_history()

        case "3":
            delete_search_history()  

        case "4":
            clear_search_history()    

        case "5" :
            print("Exiting Now !")
            print("Thank you for choosing ShopWise !")
            break       

        case _:
            print("Kindly Enter a Valid Choice") 
            pause()
            


