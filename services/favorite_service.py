from utils import pause
from database import (
    get_favorites,
    delete_favorite
)

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