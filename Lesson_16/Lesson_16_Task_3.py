class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.cash = 0

    def add(self, product, amount):
        self.amount = amount
        product.price *= 1.3
        self.products[product] = self.amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        for i in self.products:
            if identifier_type == 'name' and i.name == identifier:
                i.price *= (100 - percent) / 100
                break
            elif identifier_type == 'type' and i.type == identifier:
                i.price *= (100 - percent) / 100
                break
    def sell_product(self, product_name, amount):
        for i in self.products:
            if i.name == product_name:
                if self.products[i] < amount:
                    raise Exception('We dont have so much of this product')
                else:
                    self.products[i] -= amount
                    self.cash += i.price * amount



    def get_income(self):
        print(self.cash)

    def get_all_products(self):
        print(self.products)

    def get_product_info(self, product_name):
        for i in self.products:
            if i.name == product_name:
                print(i, self.products[i])
                break


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
s.add(p2, 100)
s.add(p, 1000)
s.set_discount('Ramen', 30)
s.get_all_products()
s.sell_product('Ramen', 50)
s.get_income()
s.get_all_products()
s.get_product_info('Ramen')
s.sell_product('Ramen', 50)
s.get_income()
s.get_all_products()
