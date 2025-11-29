class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:  # type: ignore
        # ИСПРАВЛЕНИЕ: используем type() с is not вместо !=
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return (self.__price * self.quantity) + (other.__price * other.quantity)  # type: ignore

    @classmethod
    def new_product(cls, product_date: dict) -> "Product":
        name = product_date.get("name")
        description = product_date.get("description")
        price = product_date.get("price")
        quantity = product_date.get("quantity")
        return cls(name, description, price, quantity)  # type: ignore

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
