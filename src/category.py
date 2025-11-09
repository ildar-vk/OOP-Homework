class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        # Увеличиваем общий счетчик товаров на количество товаров в этой категории
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет товар в категорию"""
        self.__products.append(product)
        # Увеличиваем общий счетчик товаров при добавлении
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку с информацией о всех товарах категории"""
        products_str = []
        for product in self.__products:
            product_info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            products_str.append(product_info)
        return "\n".join(products_str)

    def __len__(self):
        """Возвращает количество товаров в категории"""
        return len(self.__products)

    @property
    def products_list(self):
        """Возвращает список объектов товаров (для внутреннего использования)"""
        return self.__products
