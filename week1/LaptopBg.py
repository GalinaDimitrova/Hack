class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        profit = self.final_price - self.stock_price
        return profit


class Laptop(Product):

    def __init__(self, name, stock_price, final_rice, diskspace, RAM):
        super().__init__(name, stock_price, final_rice)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):

    def __init__(self, name, stock_price, final_rice, display_size, mega_pixels):
        super().__init__(name, stock_price, final_rice)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.income = 0

    def load_new_products(self, product, count):
        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, product_class):
        for product in self.products:
            if isinstance(product, product_class):
                print("{} - {}".format(product.name, self.products[product]))

    def sell_product(self, product):
        if product in self.products:
            if self.products[product] > 0:
                self.products[product] -= 1
                self.income += product.profit()
                return True

        return False

    def total_income(self):
        return self.income


store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)
store.sell_product(smarthphone)  # True
print(store.sell_product(smarthphone))  # True

print(store.total_income())  # 640
