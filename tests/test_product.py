import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counts() -> None:
    """Сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


class TestProduct:

    def test_product_initialization(self) -> None:
        """Тест корректности инициализации продукта"""
        product = Product("Test Product", "Test Description", 1000.0, 10)

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 1000.0
        assert product.quantity == 10

    def test_product_attributes_types(self) -> None:
        """Тест типов атрибутов продукта"""
        product = Product("Test", "Test", 1000.0, 10)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)
