import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
        self.response = requests.get(url = self.url, headers = self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        #title = self.soup.find("div", {"class": "o-eqqVmt o-jjpuv o-eZTujG"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        price = self.soup.find("span", {"class": "a-price-whole"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag not found"

device = PriceTracer(url="https://www.amazon.in/Samsung-Waterfall-sAMOLED-Display-Security/dp/B0CHJ4CS3K/ref=sr_1_3?crid=1QSWRGU8PBF4&keywords=samsung%2Bmobile&nsdOptOutParam=true&qid=1697576030&sprefix=sam%2Caps%2C351&sr=8-3&th=1")
print("Product: ", device.product_title())
print("Price: ", device.product_price())

#device = PriceTracer(url="https://www.amazon.in/Samsung-Galaxy-Purple-256GB-Storage/dp/B0CJ4T35VG/ref=sr_1_4?crid=1QSWRGU8PBF4&keywords=samsung%2Bmobile&nsdOptOutParam=true&qid=1697576030&sprefix=sam%2Caps%2C351&sr=8-4&th=1")
#print("Product: ", device.product_title())
#print("Price: ", device.product_price())
