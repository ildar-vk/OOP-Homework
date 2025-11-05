import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counts():
    """Сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


class TestMain:
    """Тесты для основного модуля main.py"""

    def test_product_creation_like_in_main(self):
        """Тест создания продуктов как в main"""
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        assert product1.name == "Samsung Galaxy S23 Ultra"
        assert product2.name == "Iphone 15"
        assert product3.name == "Xiaomi Redmi Note 11"
        assert product1.price == 180000.0
        assert product2.price == 210000.0
        assert product3.price == 31000.0

    def test_category_creation_like_in_main(self):
        """Тест создания категорий как в main"""
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3],
        )

        assert category1.name == "Смартфоны"
        assert len(category1.products) == 3
        assert Category.category_count == 1
        assert Category.product_count == 3

    def test_category_counts_like_in_main(self):
        """Тест счетчиков категорий и продуктов как в main"""
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category("Смартфоны", "Описание", [product1, product2, product3])

        product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
        category2 = Category("Телевизоры", "Описание", [product4])

        assert Category.category_count == 2
        assert Category.product_count == 4

    def test_main_scenario_validation(self):
        """Тест полного сценария как в main"""
        # Создаем продукты
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        # Проверяем атрибуты продуктов
        assert product1.name == "Samsung Galaxy S23 Ultra"
        assert product1.description == "256GB, Серый цвет, 200MP камера"
        assert product1.price == 180000.0
        assert product1.quantity == 5

        # Создаем категорию
        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3],
        )

        # Проверяем категорию
        assert category1.name == "Смартфоны"
        assert len(category1.products) == 3

        # Создаем вторую категорию
        product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
        category2 = Category(
            "Телевизоры",
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            [product4],
        )

        # Проверяем итоговые счетчики
        assert Category.category_count == 2
        assert Category.product_count == 4

    def test_main_function_execution(self, capsys):
        """Тест непосредственного выполнения функции main()"""
        # Импортируем и выполняем main функцию
        from src.main import main
        main()

        # Перехватываем вывод
        captured = capsys.readouterr()
        output = captured.out

        # Проверяем что вывод содержит ожидаемые данные
        lines = output.split('\n')

        # Проверяем вывод продуктов
        assert "Samsung Galaxy S23 Ultra" in output
        assert "Iphone 15" in output
        assert "Xiaomi Redmi Note 11" in output
        assert "180000.0" in output
        assert "210000.0" in output
        assert "31000.0" in output

        # Проверяем вывод категорий
        assert "Смартфоны" in output
        assert "Телевизоры" in output
        assert "True" in output  # для проверки category1.name == "Смартфоны"