from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        # name: str
        # description: str
        # category_count: int
        # product_count: int
        # products: list

        self.name = name
        self.description = description
        self.__products = products


    def add_product(self, product):
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self) -> list:
        products = []
        for product in self.__products:
            product_inform = f'{product.name}, {product.price}. Остаток: {self.product_count})'
            products.append(product_inform)
        return products




