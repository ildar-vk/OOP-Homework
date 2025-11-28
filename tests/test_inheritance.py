import pytest
import sys
import os

# Добавляем путь к src для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.product import Product, Smartphone, LawnGrass
from src.category import Category


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_creation(self):
        """Тест создания смартфона"""
        smartphone = Smartphone(
            "Test Phone", "Test Description", 1000.0, 5,
            95.5, "Test Model", 256, "Black"
        )

        assert smartphone.name == "Test Phone"
        assert smartphone.description == "Test Description"
        assert smartphone.price == 1000.0
        assert smartphone.quantity == 5
        assert smartphone.efficiency == 95.5
        assert smartphone.model == "Test Model"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"

    def test_smartphone_inheritance(self):
        """Тест что Smartphone наследуется от Product"""
        smartphone = Smartphone("Test", "Desc", 1000.0, 5, 95.5, "Model", 256, "Black")
        assert isinstance(smartphone, Product)

    def test_smartphone_str(self):
        """Тест строкового представления смартфона"""
        smartphone = Smartphone("Phone", "Desc", 1500.0, 3, 95.5, "Model", 256, "Black")
        expected = "Phone, 1500.0 руб. Остаток: 3 шт."
        assert str(smartphone) == expected


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_lawn_grass_creation(self):
        """Тест создания газонной травы"""
        grass = LawnGrass(
            "Test Grass", "Test Description", 500.0, 10,
            "Russia", "7 days", "Green"
        )

        assert grass.name == "Test Grass"
        assert grass.description == "Test Description"
        assert grass.price == 500.0
        assert grass.quantity == 10
        assert grass.country == "Russia"
        assert grass.germination_period == "7 days"
        assert grass.color == "Green"

    def test_lawn_grass_inheritance(self):
        """Тест что LawnGrass наследуется от Product"""
        grass = LawnGrass("Test", "Desc", 500.0, 10, "Russia", "7 days", "Green")
        assert isinstance(grass, Product)

    def test_lawn_grass_str(self):
        """Тест строкового представления газонной травы"""
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "USA", "5 days", "Dark Green")
        expected = "Grass, 300.0 руб. Остаток: 5 шт."
        assert str(grass) == expected


class TestProductAddition:
    """Тесты для сложения продуктов"""

    def test_smartphone_addition_same_type(self):
        """Тест сложения смартфонов одного типа"""
        phone1 = Smartphone("Phone1", "Desc", 1000.0, 2, 95.5, "Model1", 128, "Black")
        phone2 = Smartphone("Phone2", "Desc", 1500.0, 3, 98.2, "Model2", 256, "White")

        result = phone1 + phone2
        expected = (1000.0 * 2) + (1500.0 * 3)  # 2000 + 4500 = 6500
        assert result == expected

    def test_lawn_grass_addition_same_type(self):
        """Тест сложения газонных трав одного типа"""
        grass1 = LawnGrass("Grass1", "Desc", 300.0, 5, "Russia", "7 days", "Green")
        grass2 = LawnGrass("Grass2", "Desc", 400.0, 3, "USA", "5 days", "Dark Green")

        result = grass1 + grass2
        expected = (300.0 * 5) + (400.0 * 3)  # 1500 + 1200 = 2700
        assert result == expected

    def test_product_addition_same_type(self):
        """Тест сложения обычных продуктов одного типа"""
        product1 = Product("Product1", "Desc", 100.0, 4)
        product2 = Product("Product2", "Desc", 200.0, 2)

        result = product1 + product2
        expected = (100.0 * 4) + (200.0 * 2)  # 400 + 400 = 800
        assert result == expected

    def test_smartphone_lawn_grass_addition_error(self):
        """Тест ошибки при сложении смартфона и газонной травы"""
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "Russia", "7 days", "Green")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            phone + grass

    def test_product_smartphone_addition_error(self):
        """Тест ошибки при сложении обычного продукта и смартфона"""
        product = Product("Product", "Desc", 100.0, 4)
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            product + phone

    def test_product_lawn_grass_addition_error(self):
        """Тест ошибки при сложении обычного продукта и газонной травы"""
        product = Product("Product", "Desc", 100.0, 4)
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "Russia", "7 days", "Green")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            product + grass

    def test_smartphone_product_addition_error(self):
        """Тест ошибки при сложении смартфона и обычного продукта"""
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")
        product = Product("Product", "Desc", 100.0, 4)

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            phone + product

    def test_lawn_grass_product_addition_error(self):
        """Тест ошибки при сложении газонной травы и обычного продукта"""
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "Russia", "7 days", "Green")
        product = Product("Product", "Desc", 100.0, 4)

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            grass + product


class TestCategoryWithInheritance:
    """Тесты для Category с классами-наследниками"""

    def test_category_add_smartphone(self):
        """Тест добавления смартфона в категорию"""
        category = Category("Test", "Test", [])
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")

        category.add_product(phone)
        assert len(category) == 1
        assert category.products_list[0] == phone

    def test_category_add_lawn_grass(self):
        """Тест добавления газонной травы в категорию"""
        category = Category("Test", "Test", [])
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "Russia", "7 days", "Green")

        category.add_product(grass)
        assert len(category) == 1
        assert category.products_list[0] == grass

    def test_category_add_product(self):
        """Тест добавления обычного продукта в категорию"""
        category = Category("Test", "Test", [])
        product = Product("Product", "Desc", 100.0, 4)

        category.add_product(product)
        assert len(category) == 1
        assert category.products_list[0] == product

    def test_category_add_invalid_type(self):
        """Тест ошибки при добавлении не-продукта в категорию"""
        category = Category("Test", "Test", [])

        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product("not a product")

    def test_category_add_none(self):
        """Тест ошибки при добавлении None в категорию"""
        category = Category("Test", "Test", [])

        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product(None)

    def test_category_add_number(self):
        """Тест ошибки при добавлении числа в категорию"""
        category = Category("Test", "Test", [])

        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product(123)

    def test_category_initialization_with_mixed_products(self):
        """Тест инициализации категории со смешанными продуктами"""
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "Russia", "7 days", "Green")
        product = Product("Product", "Desc", 100.0, 4)

        category = Category("Mixed", "Mixed products", [phone, grass, product])

        assert len(category) == 3
        assert category.products_list[0] == phone
        assert category.products_list[1] == grass
        assert category.products_list[2] == product

    def test_category_initialization_with_invalid_products(self):
        """Тест ошибки при инициализации категории с невалидными продуктами"""
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")

        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            Category("Invalid", "Invalid products", [phone, "invalid product"])


class TestIntegration:
    """Интеграционные тесты"""

    def test_main_scenario(self):
        """Тест основного сценария из main.py"""
        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
            180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )
        smartphone2 = Smartphone(
            "Iphone 15", "512GB, Gray space", 210000.0, 8,
            98.2, "15", 512, "Gray space"
        )

        grass1 = LawnGrass(
            "Газонная трава", "Элитная трава для газона", 500.0, 20,
            "Россия", "7 дней", "Зеленый"
        )

        # Проверка атрибутов смартфона
        assert smartphone1.name == "Samsung Galaxy S23 Ultra"
        assert smartphone1.price == 180000.0
        assert smartphone1.efficiency == 95.5
        assert smartphone1.model == "S23 Ultra"

        # Проверка атрибутов газонной травы
        assert grass1.name == "Газонная трава"
        assert grass1.price == 500.0
        assert grass1.country == "Россия"
        assert grass1.germination_period == "7 дней"

        # Проверка сложения одинаковых типов
        smartphone_sum = smartphone1 + smartphone2
        expected_smartphone_sum = (180000.0 * 5) + (210000.0 * 8)
        assert smartphone_sum == expected_smartphone_sum

        # Проверка ошибки при сложении разных типов
        with pytest.raises(TypeError):
            smartphone1 + grass1

        # Проверка добавления в категорию
        category = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
        assert len(category) == 2

        # Проверка ошибки при добавлении не-продукта
        with pytest.raises(TypeError):
            category.add_product("Not a product")


if __name__ == "__main__":
    pytest.main()