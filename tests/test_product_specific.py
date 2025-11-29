import pytest
from src.product import Product, Smartphone, LawnGrass


class TestProductSpecific:
    """Целевые тесты для конкретных непокрытых строк в product.py"""

    def test_product_add_type_checking(self) -> None:
        """Тест проверки типов в __add__ (строки 19-23)"""
        product = Product("Product", "Desc", 100.0, 2)
        smartphone = Smartphone("Phone", "Desc", 1000.0, 3, 95.5, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 300.0, 4, "Russia", "7 days", "Green")

        # Product + Smartphone - должна быть ошибка
        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            product + smartphone

        # Product + LawnGrass - должна быть ошибка
        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            product + grass

        # Smartphone + Product - должна быть ошибка
        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            smartphone + product

        # LawnGrass + Product - должна быть ошибка
        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            grass + product

    def test_product_add_same_class_success(self) -> None:
        """Тест успешного сложения одинаковых классов"""
        product1 = Product("Product1", "Desc", 100.0, 2)
        product2 = Product("Product2", "Desc", 200.0, 3)

        # Product + Product - должно работать
        result = product1 + product2
        expected = (100.0 * 2) + (200.0 * 3)
        assert result == expected

    def test_smartphone_add_same_class_success(self) -> None:
        """Тест успешного сложения смартфонов"""
        phone1 = Smartphone("Phone1", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")
        phone2 = Smartphone("Phone2", "Desc", 1500.0, 3, 98.2, "Model", 256, "White")

        # Smartphone + Smartphone - должно работать
        result = phone1 + phone2
        expected = (1000.0 * 2) + (1500.0 * 3)
        assert result == expected

    def test_lawn_grass_add_same_class_success(self) -> None:
        """Тест успешного сложения газонной травы"""
        grass1 = LawnGrass("Grass1", "Desc", 300.0, 5, "Russia", "7 days", "Green")
        grass2 = LawnGrass("Grass2", "Desc", 400.0, 3, "USA", "5 days", "Dark Green")

        # LawnGrass + LawnGrass - должно работать
        result = grass1 + grass2
        expected = (300.0 * 5) + (400.0 * 3)
        assert result == expected

    def test_product_new_product_method(self) -> None:
        """Тест метода new_product"""
        product_data = {"name": "Test Product", "description": "Test Description", "price": 100.0, "quantity": 5}

        product = Product.new_product(product_data)

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 100.0
        assert product.quantity == 5

    def test_product_price_property(self) -> None:
        """Тест свойства price"""
        product = Product("Test", "Desc", 100.0, 5)

        # Проверяем геттер
        assert product.price == 100.0

        # Проверяем сеттер с корректным значением
        product.price = 150.0
        assert product.price == 150.0

    def test_product_price_validation(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Тест валидации цены"""
        product = Product("Test", "Desc", 100.0, 5)

        # Некорректные значения
        product.price = -50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевой или отрицательной" in captured.out
        assert product.price == 100.0  # Цена не изменилась

        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевой или отрицательной" in captured.out
        assert product.price == 100.0  # Цена не изменилась
