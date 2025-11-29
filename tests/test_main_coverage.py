import pytest

from src.category import Category
from src.product import LawnGrass, Smartphone


class TestMainCoverage:
    """Тесты для покрытия кода в main.py"""

    def test_main_smartphone_creation(self) -> None:
        """Тест создания смартфонов как в main.py"""
        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

        # Проверяем все атрибуты smartphone1
        assert smartphone1.name == "Samsung Galaxy S23 Ultra"
        assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
        assert smartphone1.price == 180000.0
        assert smartphone1.quantity == 5
        assert smartphone1.efficiency == 95.5
        assert smartphone1.model == "S23 Ultra"
        assert smartphone1.memory == 256
        assert smartphone1.color == "Серый"

        # Проверяем все атрибуты smartphone2
        assert smartphone2.name == "Iphone 15"
        assert smartphone2.description == "512GB, Gray space"
        assert smartphone2.price == 210000.0
        assert smartphone2.quantity == 8
        assert smartphone2.efficiency == 98.2
        assert smartphone2.model == "15"
        assert smartphone2.memory == 512
        assert smartphone2.color == "Gray space"

        # Проверяем все атрибуты smartphone3
        assert smartphone3.name == "Xiaomi Redmi Note 11"
        assert smartphone3.description == "1024GB, Синий"
        assert smartphone3.price == 31000.0
        assert smartphone3.quantity == 14
        assert smartphone3.efficiency == 90.3
        assert smartphone3.model == "Note 11"
        assert smartphone3.memory == 1024
        assert smartphone3.color == "Синий"

    def test_main_lawn_grass_creation(self) -> None:
        """Тест создания газонной травы как в main.py"""
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

        # Проверяем все атрибуты grass1
        assert grass1.name == "Газонная трава"
        assert grass1.description == "Элитная трава для газона"
        assert grass1.price == 500.0
        assert grass1.quantity == 20
        assert grass1.country == "Россия"
        assert grass1.germination_period == "7 дней"
        assert grass1.color == "Зеленый"

        # Проверяем все атрибуты grass2
        assert grass2.name == "Газонная трава 2"
        assert grass2.description == "Выносливая трава"
        assert grass2.price == 450.0
        assert grass2.quantity == 15
        assert grass2.country == "США"
        assert grass2.germination_period == "5 дней"
        assert grass2.color == "Темно-зеленый"

    def test_main_addition_operations(self) -> None:
        """Тест операций сложения как в main.py"""
        smartphone1 = Smartphone("Phone1", "Desc", 180000.0, 5, 95.5, "Model", 256, "Color")
        smartphone2 = Smartphone("Phone2", "Desc", 210000.0, 8, 98.2, "Model", 512, "Color")

        grass1 = LawnGrass("Grass1", "Desc", 500.0, 20, "Russia", "7 дней", "Green")
        grass2 = LawnGrass("Grass2", "Desc", 450.0, 15, "USA", "5 дней", "Dark Green")

        # Сложение смартфонов
        smartphone_sum = smartphone1 + smartphone2
        expected_smartphone_sum = (180000.0 * 5) + (210000.0 * 8)
        assert smartphone_sum == expected_smartphone_sum

        # Сложение газонной травы
        grass_sum = grass1 + grass2
        expected_grass_sum = (500.0 * 20) + (450.0 * 15)
        assert grass_sum == expected_grass_sum

        # Ошибка при сложении разных типов
        with pytest.raises(TypeError):
            smartphone1 + grass1

    def test_main_category_operations(self) -> None:
        """Тест операций с категориями как в main.py"""
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "Desc", 180000.0, 5, 95.5, "Model", 256, "Color")
        smartphone2 = Smartphone("Iphone 15", "Desc", 210000.0, 8, 98.2, "Model", 512, "Color")
        smartphone3 = Smartphone("Xiaomi Redmi Note 11", "Desc", 31000.0, 14, 90.3, "Model", 1024, "Color")

        grass1 = LawnGrass("Газонная трава", "Desc", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Desc", 450.0, 15, "США", "5 дней", "Темно-зеленый")

        # Создание категорий
        category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
        category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

        # Проверяем начальное состояние
        assert len(category_smartphones) == 2
        assert len(category_grass) == 2

        # Добавление продукта в категорию
        initial_count = Category.product_count
        category_smartphones.add_product(smartphone3)
        assert len(category_smartphones) == 3
        assert Category.product_count == initial_count + 1

        # Проверяем вывод продуктов
        products_str = category_smartphones.products
        assert "Samsung Galaxy S23 Ultra" in products_str
        assert "Iphone 15" in products_str
        assert "Xiaomi Redmi Note 11" in products_str

        # Ошибка при добавлении не-продукта
        with pytest.raises(TypeError):
            category_smartphones.add_product("Not a product")  # type: ignore

    def test_main_complete_flow(self) -> None:
        """Полный тест потока выполнения как в main.py"""
        # Создание всех объектов
        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

        # Проверка всех операций последовательно
        # 1. Проверка атрибутов (эмулируем print из main.py)
        assert smartphone1.name == "Samsung Galaxy S23 Ultra"
        assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
        assert smartphone1.price == 180000.0
        assert smartphone1.quantity == 5
        assert smartphone1.efficiency == 95.5
        assert smartphone1.model == "S23 Ultra"
        assert smartphone1.memory == 256
        assert smartphone1.color == "Серый"

        # 2. Сложение
        smartphone_sum = smartphone1 + smartphone2
        assert smartphone_sum == 2580000.0

        grass_sum = grass1 + grass2
        assert grass_sum == 16750.0

        # 3. Ошибка сложения разных типов
        try:
            _ = smartphone1 + grass1
            assert False, "Should have raised TypeError"
        except TypeError:
            pass  # Ожидаемое поведение

        # 4. Работа с категориями
        category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
        category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])
        assert len(category_grass) == 2
        # 5. Добавление продукта
        category_smartphones.add_product(smartphone3)

        # 6. Проверка вывода
        products_output = category_smartphones.products
        assert "Samsung Galaxy S23 Ultra" in products_output
        assert "Iphone 15" in products_output
        assert "Xiaomi Redmi Note 11" in products_output

        # 7. Проверка счетчика
        assert Category.product_count >= 5

        # 8. Ошибка добавления не-продукта
        try:
            category_smartphones.add_product("Not a product")  # type: ignore
            assert False, "Should have raised TypeError"
        except TypeError:
            pass  # Ожидаемое поведение
