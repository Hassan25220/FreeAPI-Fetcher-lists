import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()   # Data ko json ma convert kr diya hai


    if data["success"] and "data" in data:  # is condition ma hum check kr rha hai data k under koi data varibale hai k nhi and success name koi data or variable hai kya?
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        phone = user_data["phone"]
        return username, country, phone
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
       username, country, phone = fetch_random_user_freeapi()
       print(f"Username: {username} \n Country: {country} \n Phone Number: {phone}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()