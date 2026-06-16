from utils import pause
from services.analytics_service import calculate_score

def compare_products(products):
    print("\nAVAILABLE PRODUCTS")
    print("-" * 50)

    for index, product in enumerate(products,start=1):
        print(f"{index}. {product['title']}")

    print("-" * 50)    

    try:
        first= int(input("Select First Product: "))

    except ValueError :
        print("Invalid Input ! ")
        pause()
        return 
    
    try:
        second = int(input("Select Second Product: "))

    except ValueError:
        print("Invalid input.")
        pause()
        return
    
    if first == second:
        print("Please select two different products.")
        pause()
        return

    if (first < 1 
        or first > len(products) 
        or second < 1 
        or second > len(products)):

        print("Invalid product number.")
        pause()
        return    
            
    product1 = products[first - 1]
    product2 = products[second - 1]     

    score1 = calculate_score(
    product1.get("rating", 0),
    product1.get("stock", 0))

    score2 = calculate_score(
    product2.get("rating", 0),
    product2.get("stock", 0))   

    if score1 > score2:
         winner = product1["title"]

    elif score2 > score1:
          winner = product2["title"]

    else:
      winner = "Tie"

    print("\nPRODUCT COMPARISON")
    print("-" * 50)

    print(f"Product 1 : {product1['title']}")
    print(f"Product 2 : {product2['title']}")

    print("-" * 50)

    print(f"Price  : ${product1['price']} vs ${product2['price']}")
    print(f"Rating : {product1['rating']} vs {product2['rating']}")
    print(f"Stock  : {product1['stock']} vs {product2['stock']}")

    print("-" * 50)

    print(f"ShopWise Score : {score1} vs {score2}")

    if winner == "Tie":
      print("Result : It's a Tie!")

    else:
       print(f"Winner : 🏆 {winner}")  

    pause()   