class ProductRepository:
    def __init__(self):
        self.products = []

    def __repr__(self):
        result = "\n".join([f"{product.name}: {product.quantity}" for product in self.products])
        return result

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break
