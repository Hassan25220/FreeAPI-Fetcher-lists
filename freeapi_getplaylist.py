import requests 

def fetch_playlist():
    url = "https://api.freeapi.app/api/v1/public/youtube/playlists?page=1&limit=5"
    responce = requests.get(url)
    data = responce.json()

    if data.get("success") and "data" in data:
        playlist_data = data["data"]["data"]
        total_pages = data["data"].get("totalPages")
        total_Items = data["data"].get("totalItems")
        if playlist_data:
            first_playlist = playlist_data[3]
            playlist_kind = first_playlist.get("kind")
            playlist_title = first_playlist["snippet"].get("title")
            playlist_description = first_playlist["snippet"].get("description")
            return total_pages, total_Items, playlist_kind, playlist_title, playlist_description
        else:
            raise Exception("No Playlist Data Found")
    else:
        raise Exception("Data is not Fetch")
    
def main():
    try:
        total_pages, total_items, playlist_kind, playlist_title, playlist_description = fetch_playlist()
        print(f"Playlist Kind: {playlist_kind}")
        print(f"Playlist Title: {playlist_title}")
        print(f"Playlist Description: {playlist_description}")
        print(f"Total Pages: {total_pages}")
        print(f"Total Items: {total_items}")
    except Exception as e:
        print(str(e))




if __name__ == "__main__":
    main()
