import os
import sys

from src.product import Product

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class TestProduct:
    """Тесты для класса Product"""

    def test_product_creation(self) -> None:
        """Тест создания товара"""
        product = Product("Test Product", "Test Description", 1000.0, 10)
        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 1000.0
        assert product.quantity == 10

    def test_new_product_class_method(self) -> None:
        """Тест создания товара через класс-метод"""
        product_data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 1000.0,
            "quantity": 10,
        }
        product = Product.new_product(product_data)
        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 1000.0
        assert product.quantity == 10

    def test_price_setter_positive(self) -> None:
        """Тест установки корректной цены"""
        product = Product("Test", "Test", 1000.0, 10)
        product.price = 1500.0
        assert product.price == 1500.0

    def test_price_setter_negative(self, capsys) -> None:
        """Тест установки отрицательной цены"""
        product = Product("Test", "Test", 1000.0, 10)
        product.price = -100
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевой или отрицательной" in captured.out
        assert product.price == 1000.0

    def test_price_setter_zero(self, capsys) -> None:
        """Тест установки нулевой цены"""
        product = Product("Test", "Test", 1000.0, 10)
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевой или отрицательной" in captured.out
        assert product.price == 1000.0

    def test_product_attributes(self) -> None:
        """Тест всех атрибутов товара"""
        product = Product("Phone", "Smartphone", 50000.0, 5)
        assert product.name == "Phone"
        assert product.description == "Smartphone"
        assert product.price == 50000.0
        assert product.quantity == 5

    def test_product_repr(self) -> None:
        """Тест строкового представления товара через атрибуты"""
        product = Product("Tablet", "iPad", 30000.0, 3)
        # Проверяем что все атрибуты доступны для печати
        assert hasattr(product, "name")
        assert hasattr(product, "description")
        assert hasattr(product, "price")
        assert hasattr(product, "quantity")

    # ДОБАВЛЕННЫЕ ТЕСТЫ ДЛЯ ПОЛНОГО ПОКРЫТИЯ
    def test_product_with_special_characters(self) -> None:
        """Тест товара со специальными символами"""
        product = Product("Продукт с русскими", "Описание с 'кавычками'", 123.45, 7)
        assert product.name == "Продукт с русскими"
        assert product.description == "Описание с 'кавычками'"
        assert product.price == 123.45
        assert product.quantity == 7

    def test_product_with_different_price_formats(self) -> None:
        """Тест товара с разными форматами цен"""
        test_cases = [
            (0.01, 0.01),
            (1.0, 1.0),
            (100.0, 100.0),
            (1000.0, 1000.0),
            (1000000.0, 1000000.0),
        ]

        for input_price, expected_price in test_cases:
            product = Product("Test", "Test", input_price, 1)
            assert product.price == expected_price

    def test_product_quantity_edge_cases(self) -> None:
        """Тест граничных случаев количества товара"""
        test_cases = [0, 1, 100, 1000]

        for quantity in test_cases:
            product = Product("Test", "Test", 100.0, quantity)
            assert product.quantity == quantity

    def test_multiple_price_changes(self) -> None:
        """Тест множественных изменений цены"""
        product = Product("Test", "Test", 100.0, 1)

        # Корректные изменения
        product.price = 150.0
        assert product.price == 150.0

        product.price = 200.0
        assert product.price == 200.0

        # Некорректное изменение (не должно повлиять)
        product.price = -50.0
        assert product.price == 200.0  # Осталась предыдущая цена

    def test_new_product_with_complete_data(self) -> None:
        """Тест создания товара через new_product с полными данными"""
        product_data = {
            "name": "Complete Product",
            "description": "Complete Description",
            "price": 999.99,
            "quantity": 25,
        }
        product = Product.new_product(product_data)
        assert product.name == "Complete Product"
        assert product.description == "Complete Description"
        assert product.price == 999.99
        assert product.quantity == 25
