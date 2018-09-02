from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

filename = "skateboards.csv"
f = open(filename, "w")
headers = "Product Name, Price\n"
f.write(headers)


uClient = uReq("https://www.skatehut.co.uk/skateboards/skateboard_decks")
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
# finds all skateboard decks
containers = page_soup.findAll("div", {"class": "listing_product_inner prod-inner"})
container = containers[0] # stores 1 skateboard deck - for loop later
container = container.find("div", {"class": "listing_product_desc"})
container = container.a.h3.text


for container in containers:
    container = container.find("div", {"class": "listing_product_desc"})
    product_name = container.a.h3.text

    price = container.find("span", {"class": "blu-price"})
    price = price["data-fp"]
    price = list(price)
    price[0:8:1] = ""
    x = 0
    while x < 2:
        price.pop()
        x += 1
    price.insert(0, "£")
    price = "".join(price)

    print(f"Product Name: {product_name}")
    print(f"Price: {price}\n")

    f.write(product_name + ", " + price + "\n")

f.close()
