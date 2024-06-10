# Web Scraping Price Tracer

This repository contains a Python script for web scraping product details, specifically the title and price, from Amazon using the `requests` library and `BeautifulSoup`. The script is designed to track the price of a product by extracting relevant information from its product page.

### Features

- **User-Agent Handling:** Mimics a web browser by including a user-agent header in requests.
- **Product Title Extraction:** Retrieves and displays the product title from the specified Amazon product page.
- **Product Price Extraction:** Retrieves and displays the product price from the specified Amazon product page.

### Prerequisites

- **Requests Library:** Ensure you have the `requests` library installed. You can install it using pip:
  ```sh
  pip3 install requests
  ```
- **BeautifulSoup Library:** Ensure you have `BeautifulSoup` and the parser (`lxml`) installed. You can install them using pip:
  ```sh
  pip3 install beautifulsoup4 lxml
  ```

### Usage

1. **Initialize the `PriceTracer` Class:**
   Provide the URL of the Amazon product page you want to scrape.
   
2. **Retrieve Product Details:**
   Use the `product_title` and `product_price` methods to get the product's title and price.

3. **Example Code:**
   ```python
   from requests import get
   from bs4 import BeautifulSoup

   class PriceTracer:
       def __init__(self, url):
           self.url = url
           self.user_agent = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
           self.response = requests.get(url=self.url, headers=self.user_agent).text
           self.soup = BeautifulSoup(self.response, "lxml")

       def product_title(self):
           title = self.soup.find("span", {"id": "productTitle"})
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
   ```

### Notes

- **HTML Tag IDs and Classes:** The script uses specific HTML tag IDs and classes to find elements on the page. These may change over time, so the script might need updates if Amazon modifies their HTML structure.
- **Error Handling:** The script checks if the HTML tags are found and returns a "Tag not found" message if they are not.

### Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
