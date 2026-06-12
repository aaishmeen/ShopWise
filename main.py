from utils import pause
from api_handler import get_products

from services.analytics_service import (
    calculate_score,
    get_verdict,
    analyze_product_prices,
    view_price_history
    )

from services.favorite_service import (
    view_favorites,
    remove_favorite
    )

from services.history_service import (
    view_history,
    remove_search_history,
    remove_all_search_history
    )


from services.comparison_service import (
    compare_products
    )

from database import (
    create_tables,
    add_favorite,
    add_search_history,
    add_price_record
    )

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

    action = input("\n1. View Product Details \n "
                   "2. Compare Products \n"
                   "Choose Option: ")
    
    if action == "2":
        compare_products(products)
        return
    
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

    print("Price and Search history saved successfully!")
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
            analyze_product_prices()
   
        case "9" :
            print("Exiting Now !")
            print("Thank you for choosing ShopWise !")
            break       

        case _:
            print("Kindly Enter a Valid Choice") 
            pause()
            


