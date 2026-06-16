from utils import pause
from database import (
    get_product_prices,
    get_price_history
)

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

    current_price = price_list[-1]

    if current_price < average_price:
        recommendation = "BUY NOW 🔥"

    elif current_price > average_price:
        recommendation = "WAIT ⏳"

    else:
        recommendation = "FAIR PRICE 👍"

    print("\nPRICE ANALYSIS")
    print("-" * 50)

    print(f"Highest Price : {highest_price}")    
    print(f"Lowest Price : {lowest_price}")    
    print(f"Average Price : {round(average_price,2)}") 
    print()
    print(f"Current Price : {current_price}")
    print(f"Recommendation: {recommendation}")   

    print("-" * 50)

    pause()

def analyze_product_prices():

    history = get_price_history()

    if not history:
        print("No price history found.")
        pause()
        return
    
    product_names = []

    for record in history:

        if record[1] not in product_names:
            product_names.append(record[1])

    print("\nTRACKED PRODUCTS")
    print("-" * 50)

    for index, product in enumerate(product_names, start=1):
        print(f"{index}. {product}")

    print("-" * 50) 

    try:
        selection = int(
            input("Select Product Number: ")
        )

    except ValueError:
        print("Invalid input.")
        pause()
        return       
    
    if selection < 1 or selection > len(product_names):
        print("Invalid product number.")
        pause()
        return
    
    selected_product = product_names[selection - 1]

    analyze_prices(selected_product)

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

        date = record[3].strftime("%Y-%m-%d")
        time = record[4].strftime("%H:%M:%S")

        print(
            f"{record[0]:<5}"
            f"{record[1]:<25}"
            f"${record[2]:<9}"
            f"{date:<15}"
            f"{time:<10}"
        )

    print("-" * 75)

    pause()

