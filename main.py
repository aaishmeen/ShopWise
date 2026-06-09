from utils import pause
from api_handler import get_products
from database import (create_tables,
                    add_favorite,
                    get_favorites,
                    delete_favorite,
                    add_search_history,
                    get_search_history,
                    delete_search_history,
                    clear_search_history,
                    add_price_record,
                    get_price_history,
                    get_product_prices
                        )
from datetime import datetime

def calculate_score(rating, stock):

    score = 0

    # Rating contributes up to 8 points
    score += (rating / 5) * 8

    # Stock contributes up to 2 points
    if stock > 50:
        score += 2

    elif stock > 20:
        score += 1

    return round(score, 1)

def get_verdict(score):

    if score >= 8 :
        return "EXCELLENT CHOICE !"
    
    elif score >= 6 :
        return "RECOMMENDED"
    
    elif score >= 4 :
        return "AVERAGE"
    
    else:
        return "NOT RECOMMENDED !"


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

    score =  calculate_score(
        selected_product.get("rating", 0),
        selected_product.get("stock", 0))
    
    verdict = get_verdict(score)

    print(f"ShopWise Score       : {score}/10")
    print(f"Verdict     : {verdict}")

    print("\nDescription:")
    print("-" * 50)
    print(selected_product['description'])

    print("-" * 50)

    save_favorite = input("\nSave this product to favorites? (y/n): ").lower()

    if save_favorite == "y":

        add_favorite(
        selected_product["title"],
        selected_product["category"],
        selected_product["price"]
        )

        print("Product added to favorites.")  


    current_time = datetime.now()

    date = current_time.strftime("%Y-%m-%d")
    time =  current_time.strftime("%H:%M:%S")

    add_price_record(
    selected_product["title"],
    selected_product["price"],
    date,
    time
)

    add_search_history( product_name, date,time)

    print("Search saved successfully!")
    pause()


def view_history():

    history = get_search_history()

    if not history :
        print("No Search history Found !")
        pause()
        return

       
    print('-' * 65)
    print(f"{'No.':<5} {'Product Name':<25} {'Date':<15} {'Time':<10}")
    print('-' * 65)

    for search in history:

        print(
            f"{search[0]:<5}"
            f"{search[1]:<25}"
            f"{search[2]:<15}"
            f"{search[3]:<10}"
        )
        
    print("-" * 65)    
    pause()

def view_favorites():
   
    favorites= get_favorites()
    if not favorites:
        print("No favorites found.")
        pause()
        return

    print("-" * 50)

    for favorite in favorites:

        print(f"{favorite[0]}. {favorite[1]}")
        print(f"   Category : {favorite[2]}")
        print(f"   Price    : ${favorite[3]}")
        print("-" * 50)
        print("-" * 50)

    pause()

def view_price_history():

    history = get_price_history()

    if not history:
        print("No price history found.")
        pause()
        return    

    print("-" * 75) 
    print(
         f"{'ID':<5}"
        f"{'Product Name':<25}"
        f"{'Price':<10}"
        f"{'Date':<15}"
        f"{'Time':<10}"
    )      
    print("-" * 75)

    for record in history:

        print(
            f"{record[0]:<5}"
            f"{record[1]:<25}"
            f"${record[2]:<9}"
            f"{record[3]:<15}"
            f"{record[4]:<10}"
        )

    print("-" * 75)

    pause()


def remove_favorite():

    favorites = get_favorites()

    if not favorites:
        print("No favorites found.")
        pause()
        return

    print("-" * 50)

    for favorite in favorites:

        print(f"{favorite[0]}. {favorite[1]}")
        print(f"   Category : {favorite[2]}")
        print(f"   Price    : ${favorite[3]}")
        print("-" * 50)

    try:
        favorite_id = int(
            input("Enter favorite ID to delete: ")
        )

    except ValueError:
        print("Invalid input.")
        pause()
        return

    delete_favorite(favorite_id)

    print("Favorite deleted successfully!")

    pause()
    
def remove_search_history():

    history = get_search_history()

    if not history:
        print("No Search History Found!")
        pause()
        return

    print("-" * 70)

    for search in history:
        print(f"{search[0]}. {search[1]}")

    print("-" * 70)

    try:
        history_id = int(
            input("Enter Search History ID to delete: ")
        )

    except ValueError:
        print("Invalid Input")
        pause()
        return

    delete_search_history(history_id)

    print("Search History Deleted Successfully!")

    pause()


def remove_all_search_history():

    history = get_search_history()

    if not history:
        print("No Search History Found!")
        pause()
        return

    confirm_del = input("Are you sure you want to clear all search history? (y/n): ").lower()

    if confirm_del == "y":

        clear_search_history()

        print("Search History Cleared Successfully!")

    else:
        print("Operation Cancelled!")

    pause()

def analyze_prices(product_name):

    prices =  get_product_prices(product_name)

    if not prices:
        print("No price history found.")
        pause()
        return
    
    price_list = []

    for price in prices:
        price_list.append(price[0])

    highest_price = max(price_list)
    lowest_price = min(price_list)
    average_price = sum(price_list) / len(price_list)

    print("\nPRICE ANALYSIS")
    print("-" * 50)

    print(f"Highest Price : {highest_price}")    
    print(f"Lowest Price : {lowest_price}")    
    print(f"Average Price : {round(average_price,2)}")    

    print("-" * 50)

    pause()

def menu():
    print("1. Search Product ")
    print("2. View History ")
    print("3. View Favorites")
    print("4. Delete Favorites")
    print("5. Remove Search History ")
    print("6. Remove all Search History ")
    print("7. View Price History")
    print("8. Analyze Product Prices")
    print("9. Exit ")

create_tables()

while True:
    
    print ( '-' * 35 )
    print("Welcome to ShopWise!")
    print ( '-' * 35 )

    menu()
    
    choice = input("Enter your Choice (1-9) : ")
    
    match choice :
        
        case "1" :
            search_product()

        case "2" :
            view_history()

        case "3":
            view_favorites() 

        case "4":
            remove_favorite()       

        case "5":
            remove_search_history()  

        case "6":
            remove_all_search_history()    

        case "7":
            view_price_history()    
            
        case "8":
         product_name = input("Enter Product Name: ").strip()

         analyze_prices(product_name)
   
        case "9" :
            print("Exiting Now !")
            print("Thank you for choosing ShopWise !")
            break       

        case _:
            print("Kindly Enter a Valid Choice") 
            pause()
            


