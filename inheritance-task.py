class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("цена не может быть отрицательной")
        else:
            self._price = value

    def info(self):
        return f"{self.name} - название товара {self._price} - цена товара"
    
class Electronic(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def info(self):
        return f"{self.brand}- название бренда {self.name} - название товара {self._price} - цена товара"
    
class Clothes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def info(self):
        return f"{self.size} - размер {self.name} - название товара {self._price} - цена товара"
    
class Basket:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def card(self):
        for i in self.products:
            print(i.info())
        print(f"итого: {self.sum()} тенге")

    def sum(self):
        count = 0
        for i in self.products:
            count += i.price
        return count
    
if __name__ == "__main__":
    try:
        phone = Electronic("Iphone", 300, "apple" )
        shirt = Clothes("T-shirt", 10 , "M")
        basket = Basket()
        basket.add(phone)
        basket.add(shirt)
        basket.card()
        # shirt.price = -2
    except ValueError as e:
        print("Ошибка:", e)
