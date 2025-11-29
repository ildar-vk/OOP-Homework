import pytest

from src.category import Category
from src.product import LawnGrass, Smartphone


class TestIntegrationComplete:
    """Полные интеграционные тесты"""

    def test_complete_main_scenario(self) -> None:
        """Полный тест сценария из main.py"""
        # Воспроизводим ВЕСЬ код из main.py в тесте

        # === Часть 1: Создание смартфонов ===
        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

        # Проверяем ВСЕ атрибуты ВСЕХ смартфонов
        phones = [smartphone1, smartphone2, smartphone3]
        for phone in phones:
            assert hasattr(phone, "name")
            assert hasattr(phone, "description")
            assert hasattr(phone, "price")
            assert hasattr(phone, "quantity")
            assert hasattr(phone, "efficiency")
            assert hasattr(phone, "model")
            assert hasattr(phone, "memory")
            assert hasattr(phone, "color")

        # === Часть 2: Создание газонной травы ===
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

        # Проверяем ВСЕ атрибуты ВСЕЙ травы
        grasses = [grass1, grass2]
        for grass in grasses:
            assert hasattr(grass, "name")
            assert hasattr(grass, "description")
            assert hasattr(grass, "price")
            assert hasattr(grass, "quantity")
            assert hasattr(grass, "country")
            assert hasattr(grass, "germination_period")
            assert hasattr(grass, "color")

        # === Часть 3: Сложение ===
        smartphone_sum = smartphone1 + smartphone2
        assert smartphone_sum == 2580000.0

        grass_sum = grass1 + grass2
        assert grass_sum == 16750.0

        # === Часть 4: Ошибка сложения разных типов ===
        with pytest.raises(TypeError):
            smartphone1 + grass1

        # === Часть 5: Категории ===
        category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
        category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])
        assert len(category_grass) == 2

        # === Часть 6: Добавление продукта ===
        initial_count = Category.product_count
        category_smartphones.add_product(smartphone3)
        assert Category.product_count == initial_count + 1

        # === Часть 7: Вывод продуктов ===
        products_output = category_smartphones.products
        assert isinstance(products_output, str)
        assert len(products_output) > 0

        # === Часть 8: Ошибка добавления не-продукта ===
        with pytest.raises(TypeError):
            category_smartphones.add_product("Not a product")  # type: ignore

        # === Дополнительные проверки ===
        # Проверяем строковые представления
        assert str(smartphone1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        assert str(category_smartphones) == "Смартфоны, количество продуктов: 27 шт."  # 5 + 8 + 14
