import time
import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests

from config import FILENAME,URL

counter = 0

def getEtherium(first_state):
    html_text = None

    # make counter mutable
    global counter
    counter = counter + 1


    try:
        # get Coinmarketcap html code
        html_text = requests.get(URL).text

        print(f"Try: #{counter}")

        # Create bs4 object
        soup = BeautifulSoup(html_text, 'lxml')

        # get price position with bs4
        main_info = soup.find('div', class_='n78udj-0 jskEGI')
        eth_value = main_info.find('div', class_='priceValue smallerPrice')

        # Get current time
        now = datetime.now()
        current_time = str(now.strftime("%H:%M:%S"))

        # open .csv file with "a" mode
        with open('timeline.csv', 'a', encoding="utf-8", newline='') as file:

            # init file header
            fieldnames = ['value', 'time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # state to write header
            if first_state:
                writer.writeheader()

            writer.writerow({'value': eth_value.text[1:], 'time': current_time})
            print("Done!")

    # if internet connection was lost, retry in 1 minute
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(f"Try: #{counter} - Failed")
        print('Internet connection error!!!!\nReconnect in 1 minute')
        time.sleep(60)
        pass










