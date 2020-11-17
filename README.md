# Marktplaats Scraper
This script scrapes Marktplaats based on a search query and notifies the user of new listings via Pushover.

# Features
- Sends notification to your phone when it finds a new listing (title, description, price, link)
- Filters out ads and commercial sellers when desired.
- Loads queries as it goes (no need to restart, just move a file into the queries folder)

# To do List
1. Disable notifications for first scan (currently sends 30+ pushover notifications)
2. Add mechanism to either get config from command line or file (currently commandline for Docker compatibility)
3. Add more notifcation providers (e.g. email)

# Feature requests
Feel free to create an issue if you have a feature request.


# How to install
  # Docker
  The easiest way to make this program work is Docker. A docker image based on alpine linux is available at https://github.com/jaspercardol/docker-MarktplaatsScraper

  # Linux
  1. Go to the folder where you'd like to install the program.
  2. Run the following in terminal:
  ```
  sudo apt-get update && sudo apt-get install git python3 python3-pip chromium chromium-webdriver
  git clone https://github.com/jaspercardol/MarktplaatsScraper/
  cd MarktplaatsScraper
  pip3 install -r requirements.txt
  chmod +x Main.py
  ```
  3. Edit the configuration (See "Configuration" section below)
  4. Run the program by typing the following:
  ```
  ./Main.py
  ```
  
  # Windows
   1. To install run the following in your Command prompt/Terminal

```
python3
python3 -m install selenium python-pushover
```
   2. You will need to download the Chrome WebDriver for your operating system: https://chromedriver.chromium.org/downloads
   3. Extract Chrome WebDriver to a location on your computer. I would recommend a folder without UAC protection, for example C:\chromedriver\chromedriver.exe
   
# Configuration
Open config.json to make changes to the program's configuration. The following options are available:
 1. Chrome driver path. This is the exact filepath to the chromedriver.exe you downloaded earlier. Leave untouched when using Linux.
 2. Pushover API Token: The pushover API token for your app. See: https://pushover.net/apps/build
 3. Pushover User Key: The user key of your pushover account. See: https://support.pushover.net/i7-what-is-pushover-and-how-do-i-use-it
 4. Scanning interval: The interval in seconds for scanning for new listings, 120 by default.

# How to setup a query
1. Go to Marktplaats.nl and do a search with any filters you want (e.g. price, distance, etc.)
2. Copy the URL in your browser after you have done the search.
3. In the "Queries" folder, create a file (for example: macbook.json) with the .json extension.
4. Open the file in a text editor such as Notepad, Notepad++ or another program
5. Type {"query": "[URL HERE]"} and replace [URL HERE] with the URL you copied before.
6. Save the file

# Under the hood
When the program starts, it creates a file for every query file in "Listings" to save the listings in. This is done to compare the found listings to older ones, so that it can determine which listings are actually new. Once it knows, it sends a pushover notifcation with the listing details.

# Use responsibly
This program is not affiliated with Marktplaats. It is purely made to automate searching for new items. Please be respectful towards Marktplaats and don't set the interval lower than 120 seconds.
