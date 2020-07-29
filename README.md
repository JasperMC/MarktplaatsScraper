# Marktplaats Scraper
This script scrapes Marktplaats based on a search query and notifies the user of new listings via Pushover.

Run the program by executing Main.py: python Main.py

# Requirements
Requires python (tested on v3) and some additional packages. In Command Prompt or Terminal run: pip install selenium python-pushover

# Configuration
Open config.json to make changes to the program's configuration. The following options are available:

1. Pushover API Token: The pushover API token for your app. See: https://pushover.net/apps/build
2. Pushover User Key: The user key of your pushover account. See: https://support.pushover.net/i7-what-is-pushover-and-how-do-i-use-it
3. Scanning interval: The interval in seconds for scanning for new listings, 120 by default.

# How to setup a query
1. Go to Marktplaats.nl and do a search with any filters you want (e.g. price, distance, etc.)
2. Copy the URL in your browser after you have done the search.
1. In the "Queries" folder, create a file (for example: macbook.json) with the .json extension.
2. Open the file in a text editor such as Notepad, Notepad++ or another program
3. Type {"query": "[URL HERE]"} and replace [URL HERE] with the URL you copied before.
4. Save the file

# Under the hood
When the program starts, it creates a file for every query file in "Listings" to save the listings in. This is done to compare the found listings to older ones, so that it can determine which listings are actually new. Once it knows, it sends a pushover notifcation with the listing details.

# Use responsibly
This program is not affiliated with Marktplaats. It is purely made to automate searching for new items. Please be respectful towards Marktplaats and don't set the interval lower than 120 seconds.
