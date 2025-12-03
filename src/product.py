from abc import ABC, abstractmethod


class LogMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Отложим логирование до момента, когда все параметры установлены
        # Будем вызывать явно из каждого класса

    def _log_creation(self, params: list):
        """Логирует создание объекта с переданными параметрами"""
        class_name = self.__class__.__name__
        print(f"{class_name}({', '.join(params)})")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={repr(self.name)})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass


class Product(LogMixin, BaseProduct):
    """Класс продукта с множественным наследованием"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        print(f"DEBUG: Product.__init__ начат")
        # Вызываем конструкторы родителей
        super().__init__(name, description, price, quantity)
        self.__price = price

        # Логируем создание ТОЛЬКО для базового Product
        # (для наследников логирование будет в их собственных конструкторах)
        if self.__class__.__name__ == 'Product':
            params = [
                repr(self.name),
                repr(self.description),
                str(float(self.price)),
                str(self.quantity)
            ]
            self._log_creation(params)

        print(f"DEBUG: Product.__init__ завершен")

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            self.__price = value


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:
        print(f"DEBUG: Smartphone.__init__ начат")

        # Сохраняем дополнительные параметры
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        # Вызываем конструктор родителя
        super().__init__(name, description, price, quantity)

        # Логируем создание с ВСЕМИ параметрами
        params = [
            repr(self.name),
            repr(self.description),
            str(float(self.price)),
            str(self.quantity),
            str(self.efficiency),
            repr(self.model),
            str(self.memory),
            repr(self.color)
        ]
        self._log_creation(params)

        print(f"DEBUG: Smartphone.__init__ завершен")


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str) -> None:
        print(f"DEBUG: LawnGrass.__init__ начат")

        # Сохраняем дополнительные параметры
        self.country = country
        self.germination_period = germination_period
        self.color = color

        # Вызываем конструктор родителя
        super().__init__(name, description, price, quantity)

        # Логируем создание с ВСЕМИ параметрами
        params = [
            repr(self.name),
            repr(self.description),
            str(float(self.price)),
            str(self.quantity),
            repr(self.country),
            repr(self.germination_period),
            repr(self.color)
        ]
        self._log_creation(params)

        print(f"DEBUG: LawnGrass.__init__ завершен")