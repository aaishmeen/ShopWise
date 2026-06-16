import csv
import os

from database import (get_favorites,get_search_history,get_price_history)
from utils import pause

def export_favorites():

    favorites = get_favorites()

    if not favorites:
        print("No favorites found !")
        pause()
        return
    
    os.makedirs("exports",exist_ok=True)

    with open(
        "exports/favorites.csv","w",newline="")as file:

        writer= csv.writer(file)

        writer.writerow(
            ["ID","Title","Category","Price"]
        )

        for favorite in favorites:
            writer.writerow(favorite)

    print("Favorites exported successfully to exports/favorites.csv")   
        
    pause()


def export_search_history():

    history = get_search_history()

    if not history:
        print("No search history found.")
        pause()
        return

    os.makedirs("exports" , exist_ok=True)

    with open ("exports/search_history.csv","w",newline="")as file:

        writer =  csv.writer(file)

        writer.writerow(
            ["ID", "Product Name", "Search Date", "Search Time"]
        )

        for search in history:
            writer.writerow(search)

    print("Search history exported successfully to exports/search_history.csv")

    pause()    
    

def export_price_history():
    
    history = get_price_history()

    if not history:
        print("No Price History Found !")
        pause()
        return
    
    os.makedirs("exports",exist_ok=True)

    with open ("exports/price_history.csv","w",newline="")as file:

        writer =  csv.writer(file)

        writer.writerow(["ID","Product Name","Price","Date","Time"])

        for price in history:
            writer.writerow(price)

    print("Price history exported successfully to exports/price_history.csv")

    pause()

