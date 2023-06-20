import os
import random
import requests
from PIL import Image
import ctypes
import keyboard
from config import Query, ApiKey, PurityLevel, KeyBind



def main():
    wallpaper_url = get_random_wallpaper_url()  # Retrieve a random wallpaper URL from the Wallhaven API
    download_path = os.path.join(os.path.expanduser("~"), "wallpaper.jpg")

    # Download the wallpaper image
    response = requests.get(wallpaper_url)
    with open(download_path, "wb") as f:
        f.write(response.content)

    # Set the downloaded image as the desktop wallpaper
    set_wallpaper(download_path)

    print("Voila! Your desktop wallpaper has been changed to " + Query)

def get_random_wallpaper_url():
    api_url = "https://wallhaven.cc/api/v1/search?sorting=random&apikey=" + ApiKey + "&purity=" + PurityLevel + "&q=" + Query

    response = requests.get(api_url)
    data = response.json()

    # Retrieve the URL of the first wallpaper from the API response
    if "data" in data and len(data["data"]) > 0:
        return data["data"][0]["path"]

    raise Exception("Failed to retrieve a random wallpaper URL from the Wallhaven API.")

def set_wallpaper(image_path):
    # Set the downloaded image as the desktop wallpaper using ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def change_wallpaper_on_keypress():
    keyboard.add_hotkey(KeyBind, main)  # Define the key combination to trigger wallpaper change

    # Keep the program running until the hotkey is pressed
    keyboard.wait()

if __name__ == "__main__":
    change_wallpaper_on_keypress()
