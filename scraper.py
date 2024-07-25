import requests
from bs4 import BeautifulSoup
from textblob import TextBlob



# Make a get requests
data = requests.get("https://www.goodreads.com/book/show/7670800-clementine")

# Add content
data_scraping = BeautifulSoup(data.content, "html.parser")

# Select elements with class price_color
price_data = data_scraping.select("div.TruncatedContent__text")


# Loop through all the data
for price in price_data:
  print(price.text)
  text = TextBlob(price.text)
  polarity = text.sentiment.polarity
  print("Polarity: ",polarity)