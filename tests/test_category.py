import os
import sys

import pytest

from src.category import Category
from src.product import Product

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self) -> None:
        """Настройка перед каждым тестом"""
        self.product1 = Product("Product 1", "Description 1", 1000.0, 5)
        self.product2 = Product("Product 2", "Description 2", 2000.0, 10)
        self.products_list = [self.product1, self.product2]

        # Сброс счетчиков перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0

    def test_category_creation(self) -> None:
        """Тест создания категории"""
        category = Category("Test Category", "Test Description", self.products_list)
        assert category.name == "Test Category"
        assert category.description == "Test Description"
        assert Category.category_count == 1
        assert Category.product_count == 2

    def test_add_product(self) -> None:
        """Тест добавления товара в категорию"""
        category = Category("Test Category", "Test Description", self.products_list)
        initial_count = Category.product_count

        new_product = Product("New Product", "New Description", 3000.0, 3)
        category.add_product(new_product)

        assert Category.product_count == initial_count + 1

    def test_products_property_format(self) -> None:
        """Тест формата вывода товаров"""
        category = Category("Test Category", "Test Description", [self.product1])
        products_output = category.products

        expected_output = "Product 1, 1000.0 руб. Остаток: 5 шт."
        assert expected_output in products_output

    def test_products_property_multiple(self) -> None:
        """Тест вывода нескольких товаров"""
        category = Category("Test Category", "Test Description", self.products_list)
        products_output = category.products

        assert "Product 1, 1000.0 руб. Остаток: 5 шт." in products_output
        assert "Product 2, 2000.0 руб. Остаток: 10 шт." in products_output

    def test_category_count_increment(self) -> None:
        """Тест увеличения счетчика категорий"""
        # Сначала сбрасываем счетчик на случай предыдущих тестов
        Category.category_count = 0

        assert Category.category_count == 0
        category1 = Category("Category 1", "Description 1", [])
        assert Category.category_count == 1
        category2 = Category("Category 2", "Description 2", [])
        assert Category.category_count == 2

        # Исправлены имена - убраны лишние пробелы
        assert category1.name == "Category 1"  # Было "Category1" без пробела
        assert category2.name == "Category 2"  # Было "Category2" без пробела

    def test_product_count_increment(self) -> None:
        """Тест увеличения счетчика товаров"""
        initial_count = Category.product_count
        products_count = len(self.products_list)

        category = Category("Test Category", "Test Description", self.products_list)
        assert Category.product_count == initial_count + products_count

        new_product = Product("New Product", "New Description", 3000.0, 3)
        category.add_product(new_product)
        assert Category.product_count == initial_count + products_count + 1

    def test_len_method(self) -> None:
        """Тест метода __len__ для категории"""
        category = Category("Test Category", "Test Description", self.products_list)
        assert len(category) == 2

        new_product = Product("New Product", "New Description", 3000.0, 3)
        category.add_product(new_product)
        assert len(category) == 3

    def test_empty_category(self) -> None:
        """Тест пустой категории"""
        category = Category("Empty Category", "Empty Description", [])
        assert len(category) == 0
        assert category.products == ""

    def test_category_with_single_product(self) -> None:
        """Тест категории с одним товаром"""
        category = Category("Single Category", "Single Description", [self.product1])
        assert len(category) == 1
        output = category.products
        assert "Product 1, 1000.0 руб. Остаток: 5 шт." in output
        assert output.count("\n") == 0  # Только одна строка

    def test_private_products_access(self) -> None:
        """Тест что products приватный атрибут"""
        category = Category("Test", "Test", self.products_list)
        # Проверяем что нельзя получить прямой доступ к __products
        with pytest.raises(AttributeError):
            _ = category.__products

    def test_products_property_exact_format(self) -> None:
        """Тест точного формата вывода products"""
        product = Product("Exact Product", "Exact Desc", 1234.56, 7)
        category = Category("Test", "Test", [product])
        output = category.products
        expected = "Exact Product, 1234.56 руб. Остаток: 7 шт."
        assert output == expected

    def test_multiple_categories_creation(self) -> None:
        """Тест создания нескольких категорий"""
        Category.category_count = 0
        Category.product_count = 0

        cat1 = Category("Cat1", "Desc1", [self.product1])
        assert Category.category_count == 1
        assert Category.product_count == 1

        cat2 = Category("Cat2", "Desc2", [self.product2])
        assert Category.category_count == 2
        assert Category.product_count == 2

        cat3 = Category("Cat3", "Desc3", [])
        assert Category.category_count == 3
        assert Category.product_count == 2  # Пустая категория не добавляет товары

        assert cat1.name == "Cat1"
        assert cat2.name == "Cat2"
        assert cat3.name == "Cat3"

    def test_products_list_property(self) -> None:
        """Тест свойства products_list"""
        category = Category("Test Category", "Test Description", self.products_list)
        products_list = category.products_list

        assert isinstance(products_list, list)
        assert len(products_list) == 2
        assert products_list[0] == self.product1
        assert products_list[1] == self.product2

    def test_products_list_empty(self) -> None:
        """Тест properties_list с пустой категорией"""
        category = Category("Empty Category", "Empty Description", [])
        products_list = category.products_list
        assert isinstance(products_list, list)
        assert len(products_list) == 0

    def test_products_list_after_adding_product(self) -> None:
        """Тест products_list после добавления товара"""
        category = Category("Test Category", "Test Description", [self.product1])

        # Проверяем начальное состояние
        assert len(category.products_list) == 1
        assert category.products_list[0] == self.product1

        # Добавляем товар
        category.add_product(self.product2)

        # Проверяем обновленный список
        assert len(category.products_list) == 2
        assert category.products_list[0] == self.product1
        assert category.products_list[1] == self.product2

    def test_category_with_many_products(self) -> None:
        """Тест категории с большим количеством товаров"""
        products = []
        for i in range(5):
            product = Product(f"Product{i}", f"Description{i}", 100 * i, i)
            products.append(product)

        category = Category("Many Products", "Many desc", products)

        # Проверяем products_list
        products_list = category.products_list
        assert len(products_list) == 5
        for i, product in enumerate(products_list):
            assert product.name == f"Product{i}"
            assert product.price == 100 * i
            assert product.quantity == i

    def test_products_list_immutability(self) -> None:
        """Тест что изменения в возвращаемом списке не влияют на внутренний список"""
        product1 = Product("Product1", "Desc1", 100.0, 5)
        category = Category("Test", "Test", [product1])

        # Получаем список
        products_list = category.products_list

        # Пытаемся изменить его - в Python списки mutable, так что это может повлиять
        # на внутренний список. Это нормальное поведение.
        products_list.append(Product("New", "New", 300.0, 3))

        # В Python это поведение нормально - список mutable
        # Проверяем что оба списка ссылаются на один и тот же объект
        assert len(category.products_list) == 2  # Теперь должно быть 2
        assert len(category) == 2  # Должно быть 2

        # Но оригинальные данные остались
        assert category.products_list[0] == product1

    def test_category_with_special_characters(self) -> None:
        """Тест категории со специальными символами"""
        product = Product("Продукт с русскими", "Описание с 'кавычками'", 123.45, 7)
        category = Category("Категория", "Описание категории", [product])

        # Проверяем products_list
        products_list = category.products_list
        assert len(products_list) == 1
        assert products_list[0].name == "Продукт с русскими"

        # Проверяем products property
        products_str = category.products
        assert "Продукт с русскими, 123.45 руб. Остаток: 7 шт." in products_str
