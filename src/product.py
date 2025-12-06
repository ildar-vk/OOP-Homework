from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Optional, cast

if TYPE_CHECKING:
    from typing import Self


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    Определяет общий интерфейс и функциональность для всех товаров.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """
        Строковое представление продукта для пользователя.

        Returns:
            Строка в формате: "Название, цена руб. Остаток: количество шт."
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Официальное строковое представление продукта для отладки.

        Returns:
            Строка, которую можно использовать для воссоздания объекта
        """
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """
        Сложение двух продуктов (общая стоимость на складе).

        Args:
            other: Другой продукт для сложения

        Returns:
            Суммарная стоимость продуктов на складе

        Raises:
            TypeError: Если продукты разных типов
        """
        pass

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        """
        Проверка равенства продуктов по названию и описанию.

        Args:
            other: Объект для сравнения

        Returns:
            True если продукты равны, False в противном случае
        """
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """
        Получение цены продукта.

        Returns:
            Цена продукта
        """
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """
        Установка цены продукта с валидацией.

        Args:
            value: Новая цена

        Raises:
            ValueError: Если цена <= 0
        """
        pass

    @abstractmethod
    def get_total_value(self) -> float:
        """
        Вычисление общей стоимости продукта на складе.

        Returns:
            Общая стоимость = цена × количество
        """
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict) -> "BaseProduct":
        """
        Фабричный метод для создания продукта из словаря данных.

        Args:
            product_data: Словарь с данными продукта

        Returns:
            Новый экземпляр продукта

        Raises:
            KeyError: Если отсутствуют обязательные поля
        """
        pass

    @abstractmethod
    def apply_discount(self, percent: float) -> None:
        """
        Применение скидки к продукту.

        Args:
            percent: Процент скидки (от 0 до 100)

        Raises:
            ValueError: Если процент скидки некорректен
        """
        pass


class LogMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Логирует создание объекта"""
        # Вызываем конструктор следующего класса
        super().__init__(*args, **kwargs)

    def _log_creation(self) -> None:
        """Логирует информацию о создании объекта"""
        class_name = self.__class__.__name__

        # Формируем строку с параметрами
        params: list[str] = []

        # Базовые параметры - проверяем через isinstance
        if isinstance(self, BaseProduct):
            params.append(repr(self.name))
            params.append(repr(self.description))
            params.append(str(self.price))
            params.append(str(self.quantity))

        # Для наследников добавляем специфические параметры
        if hasattr(self, "efficiency") and hasattr(self, "model"):
            # Это Smartphone
            params.append(str(self.efficiency))  # type: ignore[attr-defined]
            params.append(repr(self.model))  # type: ignore[attr-defined]
            params.append(str(self.memory))  # type: ignore[attr-defined]
            params.append(repr(self.color))  # type: ignore[attr-defined]
        elif hasattr(self, "country") and hasattr(self, "germination_period"):
            # Это LawnGrass
            params.append(repr(self.country))  # type: ignore[attr-defined]
            params.append(repr(self.germination_period))  # type: ignore[attr-defined]
            params.append(repr(self.color))  # type: ignore[attr-defined]

        # Выводим результат
        print(f"{class_name}({', '.join(params)})")

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки"""
        class_name = self.__class__.__name__

        if isinstance(self, BaseProduct):
            if hasattr(self, "efficiency") and hasattr(self, "model"):
                # Это Smartphone
                return (
                    f"Smartphone(name={repr(self.name)}, "
                    f"description={repr(self.description)}, "
                    f"price={self.price}, quantity={self.quantity}, "
                    f"efficiency={self.efficiency}, "  # type: ignore[attr-defined]
                    f"model={repr(self.model)}, "  # type: ignore[attr-defined]
                    f"memory={self.memory}, "  # type: ignore[attr-defined]
                    f"color={repr(self.color)})"
                )  # type: ignore[attr-defined]
            elif hasattr(self, "country") and hasattr(self, "germination_period"):
                # Это LawnGrass
                return (
                    f"LawnGrass(name={repr(self.name)}, "
                    f"description={repr(self.description)}, "
                    f"price={self.price}, quantity={self.quantity}, "
                    f"country={repr(self.country)}, "  # type: ignore[attr-defined]
                    f"germination_period={repr(self.germination_period)}, "  # type: ignore[attr-defined]
                    f"color={repr(self.color)})"
                )  # type: ignore[attr-defined]
            else:
                # Обычный Product
                return (
                    f"Product(name={repr(self.name)}, "
                    f"description={repr(self.description)}, "
                    f"price={self.price}, quantity={self.quantity})"
                )
        return f"{class_name}()"


class Product(LogMixin, BaseProduct):
    """Конкретный класс продукта с множественным наследованием"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)
        self.__price = price
        # Для обычного Product вызываем логирование здесь
        if self.__class__ == Product:
            self._log_creation()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.description == other.description and self.__price == other.__price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            # Не меняем цену, просто выходим
            return
        self.__price = price

    def get_total_value(self) -> float:
        """Общая стоимость продукта на складе"""
        return self.__price * self.quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создает новый продукт из словаря с данными"""
        required_fields = ["name", "price", "quantity"]
        for field in required_fields:
            if field not in product_data:
                raise KeyError(f"Отсутствует обязательное поле: {field}")

        name = product_data.get("name", "")
        description = product_data.get("description", "")
        price = float(product_data.get("price", 0))
        quantity = int(product_data.get("quantity", 0))

        return cls(name, description, price, quantity)

    def apply_discount(self, percent: float) -> None:
        """Применяет скидку к продукту"""
        if not 0 <= percent <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")

        discount_factor = (100 - percent) / 100
        self.__price = round(self.__price * discount_factor, 2)


class Smartphone(Product):
    """Класс смартфона - наследник Product"""

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
        # Вызываем логирование после установки всех атрибутов
        self._log_creation()

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Smartphone):
            return False
        return (
            super().__eq__(other)
            and self.efficiency == other.efficiency
            and self.model == other.model
            and self.memory == other.memory
            and self.color == other.color
        )

    def get_total_value(self) -> float:
        return self.price * self.quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Smartphone":
        required_fields = ["name", "price", "quantity", "efficiency", "model", "memory", "color"]
        for field in required_fields:
            if field not in product_data:
                raise KeyError(f"Отсутствует обязательное поле: {field}")

        return cls(
            name=str(product_data["name"]),
            description=str(product_data.get("description", "")),
            price=float(product_data["price"]),
            quantity=int(product_data["quantity"]),
            efficiency=float(product_data["efficiency"]),
            model=str(product_data["model"]),
            memory=int(product_data["memory"]),
            color=str(product_data["color"]),
        )

    def apply_discount(self, percent: float) -> None:
        if not 0 <= percent <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")
        discount_factor = (100 - percent) / 100
        self.price = round(self.price * discount_factor, 2)


class LawnGrass(Product):
    """Класс газонной травы - наследник Product"""

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
        # Вызываем логирование после установки всех атрибутов
        self._log_creation()

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, LawnGrass):
            return False
        return (
            super().__eq__(other)
            and self.country == other.country
            and self.germination_period == other.germination_period
            and self.color == other.color
        )

    def get_total_value(self) -> float:
        return self.price * self.quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "LawnGrass":
        required_fields = ["name", "price", "quantity", "country", "germination_period", "color"]
        for field in required_fields:
            if field not in product_data:
                raise KeyError(f"Отсутствует обязательное поле: {field}")

        return cls(
            name=str(product_data["name"]),
            description=str(product_data.get("description", "")),
            price=float(product_data["price"]),
            quantity=int(product_data["quantity"]),
            country=str(product_data["country"]),
            germination_period=str(product_data["germination_period"]),
            color=str(product_data["color"]),
        )

    def apply_discount(self, percent: float) -> None:
        if not 0 <= percent <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")
        discount_factor = (100 - percent) / 100
        self.price = round(self.price * discount_factor, 2)
