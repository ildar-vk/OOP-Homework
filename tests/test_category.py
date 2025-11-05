import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    """Фикстура с примером продуктов для тестов"""
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


@pytest.fixture(autouse=True)
def reset_counts():
    """Сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


class TestCategory:
    """Тесты для класса Category"""

    def test_category_initialization(self, sample_products):
        """Тест корректности инициализации категории"""
        category = Category("Test Category", "Test Description", sample_products)

        assert category.name == "Test Category"
        assert category.description == "Test Description"
        assert category.products == sample_products

    def test_category_attributes_types(self, sample_products):
        """Тест типов атрибутов категории"""
        category = Category("Test Category", "Test Description", sample_products)

        assert isinstance(category.name, str)
        assert isinstance(category.description, str)
        assert isinstance(category.products, list)

    def test_products_count_in_category(self, sample_products):
        """Тест подсчета количества продуктов в категории"""
        category = Category("Test Category", "Test Description", sample_products)

        assert len(category.products) == 3
        assert Category.product_count == 3

    def test_empty_category_products_count(self):
        """Тест пустой категории"""
        category = Category("Test Category", "Test Description", [])

        assert len(category.products) == 0
        assert Category.product_count == 0

    def test_category_count_increment(self):
        """Тест подсчета количества категорий"""
        # Начинаем с 0 из-за autouse фикстуры
        assert Category.category_count == 0

        category1 = Category("Category 1", "Description 1", [])
        assert Category.category_count == 1

        category2 = Category("Category 2", "Description 2", [])
        assert Category.category_count == 2

    def test_product_count_increment(self, sample_products):
        """Тест подсчета общего количества продуктов"""
        # Начинаем с 0 из-за autouse фикстуры
        assert Category.product_count == 0

        category1 = Category("Category 1", "Description 1", sample_products)
        assert Category.product_count == 3

        additional_products = [Product("New Product", "Desc", 500.0, 2)]
        category2 = Category("Category 2", "Description 2", additional_products)
        assert Category.product_count == 4

    def test_category_with_single_product(self):
        """Тест категории с одним продуктом"""
        product = Product("Single Product", "Description", 1000.0, 1)
        category = Category("Test Category", "Test Description", [product])

        assert len(category.products) == 1
        assert Category.product_count == 1
        assert Category.category_count == 1

    def test_combined_counts(self, sample_products):
        """Тест одновременного подсчета категорий и продуктов"""
        category1 = Category("Category 1", "Description 1", sample_products[:2])
        category2 = Category("Category 2", "Description 2", sample_products[2:])

        assert Category.category_count == 2
        assert Category.product_count == 3
        assert len(category1.products) == 2
        assert len(category2.products) == 1