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
        self.sale = 0

    def add(self, product):
        self.products.append(product)

    def delete(self, product_name):
        for i in self.products:
            if i.name.lower() == product_name.lower():
                self.products.remove(i)
                print (f"товар {product_name} удален")
            else:
                print("такого товара нет в корзине")

    def sale(self, percent):
        if percent >=0 and percent <=100:
            self.sale = percent
        else:
            raise ValueError("скидка не может быть меньше нуля или больше ста")

    def cost(self):
        count = sum(i.price for i in self.products)
        return count * (1 - self.sale / 100)
        # for i in self.products:
        #     count += i.price
        # return count

    def show(self):
        for i in self.products:
            print(i.info())
        print(f"скидка {self.sale}")
        print(f"итоговая цена {self.cost()}")

    
if __name__ == "__main__":
    try:
        phone = Electronic("Iphone", 300, "apple" )
        shirt = Clothes("T-shirt", 10 , "M")
        basket = Basket()
        basket.add(phone)
        basket.add(shirt)
        basket.sale(20)
        basket.show()
    except ValueError as e:
        print("Ошибка:", e)
