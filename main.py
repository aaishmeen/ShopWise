from utils import pause
from api_handler import get_products
from storage import (load_history, 
                     save_history, 
                     load_favorites, 
                     save_favorites)
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

    try : 
        selection = int(input("Select a product number for detailed information : "))    
  
    except ValueError:
        print("Please enter a valid number !")
        pause()
        return 
    
    if selection < 1 or selection > len(products):
        print("Invalid product number.")
        pause()
        return
    
    selected_product = products[selection -1]

    print("\n" + "-" * 50)
    print("PRODUCT DETAILS")
    print("-" * 50)

    print(f"Title       : {selected_product['title']}")
    print(f"Category    : {selected_product['category']}")
    print(f"Price       : ${selected_product['price']}")
    print(f"Rating      : {selected_product.get('rating','N/A')}")
    print(f"Stock       : {selected_product.get('stock','N/A')}")

    print("\nDescription:")
    print("-" * 50)
    print(selected_product['description'])

    print("-" * 50)

    save_favorite = input("\nSave this product to favorites? (y/n): ").lower()

    if save_favorite == "y":

        for favorite in favorites:

            if favorite["title"] == selected_product["title"]:
                print("Product already exists in favorites.")
                pause()
                return

        favorite = {
        "title": selected_product["title"],
        "category": selected_product["category"],
        "price": selected_product["price"]
        }

        favorites.append(favorite)

        save_favorites(favorites)

        print("Product added to favorites.")  




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

def view_favorites():
   
    if not favorites:
        print("No favorites found.")
        pause()
        return

    print("-" * 50)

    for index, favorite in enumerate(favorites, start=1):

        print(f"{index}. {favorite['title']}")
        print(f"   Category : {favorite['category']}")
        print(f"   Price    : ${favorite['price']}")
        print("-" * 50)

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
    print("3.View Favorites")
    print("4. Delete Search History ")
    print("5. Clear Search History ")
    print("6. Exit ")

search_history = load_history()
favorites = load_favorites()

while True:

    print ( '-' * 35 )
    print("Welcome to ShopWise!")
    print ( '-' * 35 )

    menu()
    
    choice = input("Enter your Choice (1-6) : ")
    
    match choice :
        
        case "1" :
            search_product()

        case "2" :
            view_history()

        case "3":
            view_favorites()    

        case "4":
            delete_search_history()  

        case "5":
            clear_search_history()    

        case "6" :
            print("Exiting Now !")
            print("Thank you for choosing ShopWise !")
            break       

        case _:
            print("Kindly Enter a Valid Choice") 
            pause()
            


