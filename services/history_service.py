from utils import pause
from database import (
                get_search_history,
                delete_search_history,
                clear_search_history
            )

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