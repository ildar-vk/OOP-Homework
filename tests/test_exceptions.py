# tests/test_exceptions.py

import pytest
from src.category import Category
from src.product import Product, ZeroQuantityError


class TestExceptions:
    """Тесты для обработки исключений"""

    def test_zero_quantity_product_creation(self):
        """Тест создания товара с нулевым количеством (Задание 1)"""
        with pytest.raises(ZeroQuantityError) as exc_info:
            Product("Test Product", "Description", 100.0, 0)

        assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)

    def test_zero_quantity_via_value_error(self):
        """Тест что ZeroQuantityError наследует ValueError"""
        with pytest.raises(ValueError) as exc_info:
            Product("Test Product", "Description", 100.0, 0)

        assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)

    def test_valid_product_creation(self):
        """Тест создания валидного товара"""
        product = Product("Valid Product", "Description", 100.0, 5)
        assert product.name == "Valid Product"
        assert product.quantity == 5

    def test_middle_price_with_products(self):
        """Тест расчета среднего ценника с товарами"""
        product1 = Product("Product 1", "Desc 1", 100.0, 2)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        product3 = Product("Product 3", "Desc 3", 300.0, 1)

        category = Category("Test Category", "Description", [product1, product2, product3])

        # (100 + 200 + 300) / 3 = 200
        assert category.middle_price() == 200.0

    def test_middle_price_empty_category(self):
        """Тест расчета среднего ценника для пустой категории (Задание 2)"""
        category = Category("Empty Category", "Description", [])
        assert category.middle_price() == 0.0

    def test_middle_price_single_product(self):
        """Тест расчета среднего ценника для одного товара"""
        product = Product("Single Product", "Desc", 150.0, 1)
        category = Category("Single Category", "Description", [product])
        assert category.middle_price() == 150.0

    def test_middle_price_zero_price_product(self):
        """Тест расчета среднего ценника с товаром нулевой цены"""
        product1 = Product("Product 1", "Desc 1", 0.0, 2)
        product2 = Product("Product 2", "Desc 2", 100.0, 3)

        category = Category("Test Category", "Description", [product1, product2])

        # (0 + 100) / 2 = 50
        assert category.middle_price() == 50.0

    def test_category_with_mixed_products(self):
        """Тест категории с разными типами товаров"""
        from src.product import Smartphone, LawnGrass

        smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 500.0, 3, "Russia", "14 days", "Green")

        category = Category("Mixed Category", "Description", [smartphone, grass])

        # (1000 + 500) / 2 = 750
        assert category.middle_price() == 750.0

    def test_product_creation_with_negative_quantity(self):
        """Тест создания товара с отрицательным количеством"""
        # В текущей реализации это не обрабатывается, но можно добавить
        product = Product("Test", "Desc", 100.0, -5)
        assert product.quantity == -5  # Это должно работать, но можно добавить проверку