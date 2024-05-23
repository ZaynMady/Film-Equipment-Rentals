from classes.product import product
import requests
from bs4 import BeautifulSoup
import pandas as pd

class CCR (product):
    def __init__(self, name, Type, price, image, description=None):
        self.image = image
        super().__init__(name, Type, price, "Cairo Camera Rentals")

class CCR_cam (CCR):
    def __init__(self, name: str, price, image, description=None):
        super().__init__(name, "Camera", price, image)
        self.category = "" 
    
    def check_category(self):
        if "DSLR" in self.name.upper():
            self.category = "DSLR"
        elif "Cinema" in self.name:
            self.category = "cinema"
        elif "Mirrorless" in self.name:
            self.category = "mirrorless"
        elif "360" in self.name:
            self.category = "360"
        elif "GoPro" in self.name:
            self.category = "GoPro"
        elif "Battery" in self.name:
            self.category = "Battery and Chargers"
        else:
            self.category = "None"
    
    def get_list():
        cams = list()
        #getting html using requests
        CCR_cam_url = "https://cairocamerarentals.com/dashboard/getAllEquipments/1"
        response = requests.get(CCR_cam_url)

        #parsing the request
        soup = BeautifulSoup(response.content, "html.parser")

        #getting information out of it
        soup_products = soup.select("div.product-wrapper.product-four-column")

        for soup_product in soup_products:
            #getting the name of the product
            name_tag = soup_product.find("h5")
            name = name_tag.text.strip()

            #getting the price out of it
            price_tag = soup_product.find("span", class_="amount")
            str_price = price_tag.text.strip().replace("EGP. ", "")
            price = float(str_price)

            #getting the image
            image_tag = soup_product.find("img")
            image = image_tag["src"]

            cam = CCR_cam(name=name, price=price, image=image)
            cam.check_category()
            cams.append(cam)

        return cams
    
    def get_dataframe():
        cameras = CCR_cam.get_list()

        df = pd.DataFrame(columns=["Name", "Category", "Price"])

        for camera in cameras:
            new_row = {
                "Name" : camera.name, 
                "Category" : camera.category, 
                "Price" : camera.price
            }
            new_df = pd.DataFrame([new_row])

            df = pd.concat([df, new_df], ignore_index=True)

        return df

class CCR_lighting (CCR):
    pass

