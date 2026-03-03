class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def info(self):
        print(f"Название: {self.name}, Цена:{self.price}")


class Basket:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def card(self):
        for i in self.products:
            print(f"Название: {i.name}, Цена:{i.price}")

    def all_price(self):
        count = 0
        for i in self.products:
            count += i.price
        return count
    
    def delete(self, product_name):
        for i in self.products:
            if i.name.lower() == product_name.lower():
                self.products.remove(i)
                print (f"товар {product_name} удален")
    
p1 = Product("Молоко", 500)
p2 = Product("чай", 200)
p3 = Product("Хлеб", 250)
p4 = Product("Сахар", 200)
b = Basket()
b.add(p1)
b.add(p2)
b.add(p3)
b.add(p4)
b.delete("Молоко")
b.card()
print(b.all_price())