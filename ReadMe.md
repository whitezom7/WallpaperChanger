# Wallpaper Changer

The **Wallpaper Changer** is a Python program that allows you to automatically change your desktop wallpaper using random images from the Wallhaven API. You can also set a hotkey combination to manually trigger the wallpaper change.

## Features

- Retrieves a random wallpaper URL from the Wallhaven API based on a specified search query, API key, and purity level.
- Downloads the wallpaper image from the retrieved URL.
- Sets the downloaded image as the desktop wallpaper.
- Provides an option to change the wallpaper by pressing a specific key combination.

## Installation

To run the Wallpaper Changer program, follow these steps:

1. Install Python: Make sure you have Python installed on your system. You can download the latest version of Python from the official website: [python.org](https://www.python.org/downloads/).

2. Install the required packages: Open a terminal or command prompt and navigate to the directory containing the program files. Run the following command to install the necessary packages:
  
  pip install requests pillow keyboard

3. Obtain a Wallhaven API key: Visit the [Wallhaven API](https://wallhaven.cc/help/api) page and follow the instructions to obtain an API key. Note down the API key for later use.

4. Download the program files: Download the program files from the repository or copy the provided code into a file with the `.py` extension.

5. Create a configuration file: Create a new file named `config.py` in the same directory as the program files. Open the `config.py` file in a text editor and define the following variables:

- `Query`: Specify the search query for wallpapers (e.g., "nature", "space", "cars").
- `ApiKey`: Set your Wallhaven API key obtained in step 3.
- `PurityLevel`: Choose the purity level for the wallpapers ("sfw", "sketchy", "nsfw").
- `ScreenResolution`: Choose the Screen Resolution for the wallpapers ("1280x720", "1920x1080", "2560x1440").
- `KeyBind`: Define the key combination to trigger wallpaper change (e.g., "ctrl+shift+c").

Save the `config.py` file after defining the variables.

## Usage

1. Run the program: Open a terminal or command prompt and navigate to the directory containing the program files. Run the following command to execute the program:

  python main.py

The program will start running and retrieve a random wallpaper from the Wallhaven API. It will then download and set the downloaded image as your desktop wallpaper.

2. Manually change wallpaper: If you want to manually change the wallpaper, press the key combination defined in the `KeyBind` variable in the `config.py` file. The program will immediately fetch and set a new wallpaper based on the search query.

3. Terminate the program: To stop the program, press `Ctrl+C` in the terminal or command prompt where the program is running.

## Notes

- The program uses the Wallhaven API to fetch random wallpapers. Make sure you have a stable internet connection to retrieve the wallpapers successfully.
- The downloaded wallpaper will be saved as `wallpaper.jpg` in the user's home directory (`C:\Users\<username>` on Windows).
- The program is designed to work on Windows operating systems.

