import requests

def get_products(product_name):

    url = f"https://dummyjson.com/products/search?q={product_name}"

    try:
        
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


    except requests.RequestException:
        print("Unable to fetch products.")
        return {"products": []}