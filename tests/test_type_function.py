import pytest

from src.product import LawnGrass, Product, Smartphone


class TestTypeFunctionUsage:
    """Тесты для проверки использования функции type()"""

    def test_product_uses_type_function(self) -> None:
        """Тест что Product использует type() для проверки типов"""
        product1 = Product("Product1", "Desc", 100.0, 2)
        product2 = Product("Product2", "Desc", 200.0, 3)
        smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")

        # Должно работать - одинаковые типы
        result = product1 + product2
        assert result == (100.0 * 2) + (200.0 * 3)

        # Должна быть ошибка - разные типы
        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            product1 + smartphone

    def test_smartphone_uses_type_function(self) -> None:
        """Тест что Smartphone использует type() для проверки типов"""
        phone1 = Smartphone("Phone1", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")
        phone2 = Smartphone("Phone2", "Desc", 1500.0, 3, 98.2, "Model", 256, "White")
        product = Product("Product", "Desc", 100.0, 4)

        # Должно работать - одинаковые типы
        result = phone1 + phone2
        assert result == (1000.0 * 2) + (1500.0 * 3)

        # Должна быть ошибка - разные типы
        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            phone1 + product

    def test_lawn_grass_uses_type_function(self) -> None:
        """Тест что LawnGrass использует type() для проверки типов"""
        grass1 = LawnGrass("Grass1", "Desc", 300.0, 5, "Russia", "7 days", "Green")
        grass2 = LawnGrass("Grass2", "Desc", 400.0, 3, "USA", "5 days", "Dark Green")
        smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")

        # Должно работать - одинаковые типы
        result = grass1 + grass2
        assert result == (300.0 * 5) + (400.0 * 3)

        # Должна быть ошибка - разные типы
        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            grass1 + smartphone

    def test_type_function_behavior(self) -> None:
        """Тест поведения функции type()"""
        product = Product("Product", "Desc", 100.0, 2)
        smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")

        # Проверяем что type() возвращает правильные типы (используем is)
        assert type(product) is Product
        assert type(smartphone) is Smartphone
        assert type(product) is not type(smartphone)

        # Проверяем что isinstance ведет себя иначе (наследование)
        assert isinstance(smartphone, Product)  # Smartphone является Product
        assert not type(smartphone) is Product  # Но type() возвращает точный класс


def test_main_scenario_with_type() -> None:
    """Тест основного сценария с использованием type()"""
    from src.product import LawnGrass, Smartphone

    smartphone1 = Smartphone("Phone1", "Desc", 180000.0, 5, 95.5, "Model", 256, "Color")
    smartphone2 = Smartphone("Phone2", "Desc", 210000.0, 8, 98.2, "Model", 512, "Color")
    grass1 = LawnGrass("Grass1", "Desc", 500.0, 20, "Russia", "7 дней", "Green")

    # Сложение одинаковых типов должно работать
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == (180000.0 * 5) + (210000.0 * 8)

    # Сложение разных типов должно вызывать ошибку
    with pytest.raises(TypeError):
        smartphone1 + grass1
