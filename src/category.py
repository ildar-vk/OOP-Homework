# src/category.py


from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = []  # type: ignore

        # Добавляем продукты через метод для проверки типов
        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self) -> float:
        """
        Рассчитывает средний ценник всех товаров в категории.
        Возвращает 0, если в категории нет товаров.
        """
        try:
            # Задание 2: обработка деления на ноль
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)  # type: ignore
        except ZeroDivisionError:
            return 0.0

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __len__(self) -> int:
        return len(self.__products)

    @property
    def products(self) -> str:
        products_str = []
        for product in self.__products:
            products_str.append(str(product))
        return "\n".join(products_str)

    @property
    def products_list(self) -> list[Product]:
        return self.__products
