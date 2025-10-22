"""
START

    Prompt user to enter the website URL
    Store the input as 'url'

    Send an HTTP GET request to 'url'
    Check if the request was successful
    If not, display an error and STOP

    Parse the HTML content using BeautifulSoup

    Initialize an empty list 'data_list' to store scraped data

    For each relevant HTML element (e.g., quotes container):
        Extract the specific data fields (e.g., text, author, tags)
        Store the extracted data as a dictionary
        Append the dictionary to 'data_list'

    Convert 'data_list' into a DataFrame
    Save the DataFrame as a CSV file in a 'data' folder

    Display message: "Scraping complete! Data saved."

END
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

url = input("Enter the website URL you want to scrape: ")

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    data_list = []

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").get_text(strip=True).replace("\n", " ")
        author = quote.find("small", class_="author").get_text(strip=True)
        tags = ", ".join([tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")])
        if text:  # avoid empty quotes
            data_list.append({"Quote Text": text, "Author Name": author, "Tags": tags})

    # Remove duplicates
    unique_data = {item["Quote Text"]: item for item in data_list}.values()
    df = pd.DataFrame(unique_data)

    df.to_csv("data/scraped_data.csv", index=False, encoding="utf-8")
    print("Scraping complete! Data saved to data/scraped_data.csv")

except requests.RequestException as e:
    print(f"Error fetching the page: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
