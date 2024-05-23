class product:
    def __init__(self, name, Type, price, shop, image=None, description=None):
        if type(price) is int or type(price) is float: 
            self.price = price
        else: 
            raise TypeError("Price should be of type int or Float")
        
        self.name = name
        self.type = Type
        self.shop = shop
        self.image = image
        self.description = description

    def __str__(self) -> str:
        return "Product Image: " + self.image + "\n" + "Product Name: " + self.name + "\n" + "Price: " + str(self.price) + "\n" 

        