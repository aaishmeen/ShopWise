from utils import pause

from database import (
    get_product_prices,
    get_price_history
)

def analyze_price_trend(product_name):
    
    prices =  get_product_prices(product_name)

    if not prices:
        print("No Price History Found !")
        pause()
        return
    
    price_list = []

    for price in prices  :
        price_list.append(price[0])

    if len(price_list) < 2:
        print("Not enough data for trend analysis.")
        pause()
        return
    
    first_price = price_list[0]
    latest_price = price_list[-1]

    if latest_price > first_price:
        trend = "INCREASING 📈"

    elif latest_price < first_price:
        trend = "DECREASING 📉"

    else:
        trend = "STABLE ➖"

    if trend == "INCREASING 📈":
        recommendation = ("Price is rising. Consider buying soon.")

    elif trend == "DECREASING 📉":
        recommendation = ("Price is falling. Consider waiting.")

    else:
        recommendation = ("Price is stable.")    

    print("\nPRICE TREND ANALYSIS")
    print("-" * 50)

    print(f"First Price  : {first_price}")
    print(f"Latest Price : {latest_price}")

    print()
    print(f"Trend        : {trend}")

    print()
    print(f"Recommendation: {recommendation}")

    print("-" * 50)

    pause()

def analyze_product_trend():
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

    analyze_price_trend(selected_product)