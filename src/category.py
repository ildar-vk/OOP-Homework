class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __len__(self):
        return len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products_str = []
        for product in self.__products:
            products_str.append(str(product))  # Используем __str__ продукта
        return "\n".join(products_str)

    @property
    def products_list(self):
        return self.__products
