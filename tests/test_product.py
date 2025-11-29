from src.product import Product


class Product:  # type: ignore
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if self.__class__ != other.__class__:
            raise TypeError("Нельзя складывать товары разных типов")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        # Получаем значения с проверками
        name = product_data.get("name")
        description = product_data.get("description", "")  # значение по умолчанию
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        # Проверка обязательных полей
        if not name:
            raise ValueError("Отсутствует название товара")
        if price is None:
            raise ValueError("Отсутствует цена")
        if quantity is None:
            raise ValueError("Отсутствует количество")

        # Явное преобразование типов
        return cls(  # type: ignore
            name=str(name), description=str(description), price=float(price), quantity=int(quantity)
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            self.__price = price


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
