import requests

def fetch_data_of_products():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()

    # Print the entire data to understand the structure
    # print(data)

    # Ensure we access the data correctly
    if data.get("success") and "data" in data:
        product_list = data["data"]["data"]  # Correctly access the list of products
        if len(product_list) > 0:
            first_product = product_list[6]  # Get the first product in the list
            category = first_product.get("category")
            thumbnail = first_product.get("thumbnail")
            status_code = data.get("statusCode")  # Get the status code
            return category, thumbnail, status_code
        else:
            raise Exception("No products found")
    else:
        raise Exception("Failed to fetch data")

def main():
    try:
        category, thumbnail, status_code = fetch_data_of_products()
        print(f"Category: {category}\nThumbnail: {thumbnail}\nStatus Code: {status_code}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
