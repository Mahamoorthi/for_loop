class Items():

    def __init__(self,name,description,price):
        self.name = name
        self.description = description
        self.price = price
        
    def display(self):
        return f"product name:{self.name} description: {self.description} price: {self.price}"

product1 = Items("apple","royal",20)
print("Name:",product1.name)
print("description:",product1.description)
print("price:",product1.price)
print(product1.display())


