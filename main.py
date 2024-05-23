import requests
from bs4 import BeautifulSoup
from product import product


def main():
    #getting the html
    cinemacamerasurl = "https://cairocamerarentals.com/dashboard/getShopByCategory/123"
    response = requests.get(cinemacamerasurl)
    
    #parsing it using beautiful soup
    soup = BeautifulSoup(response.content, "html.parser")

    #extracting product name and price
    #soup_products = soup.select("div.product-details")
    #extracting product image 
    soup_products = soup.select("div.product-wrapper.product-four-column")
    
    #initializing a list of products 
    products = list()

    for soup_product in soup_products:
        name_tag = soup_product.find("h5")
        price_tag = soup_product.find("span", class_="amount")
        img_tag = soup_product.find("img")

        if name_tag and price_tag and img_tag:
            #setting the name
            name = name_tag.text.strip()
            
            #setting the price
            str_price = str(price_tag.text.strip())
            str_price = str_price.replace("EGP. ", "")
            price = float(str_price)
            #setting the image
            image_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else "No image available"
            #setting the final product
            item = product(name = name, price= price, shop="Cairo Camera Rentals", Type="Camera", image=image_url)
            products.append(item)
        else:
            print("name and price not found")

    
    for _product in products:
        print(_product)




main()