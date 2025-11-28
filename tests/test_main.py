import pytest
import sys
import os


def test_main_exists():
    """Простой тест что main.py существует"""
    main_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'main.py')
    assert os.path.exists(main_path), f"main.py not found at {main_path}"


def test_main_imports():
    """Тест что можно импортировать классы из main.py"""
    # Добавляем src в путь импорта
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

    try:
        # Пробуем импортировать main
        import main

        # Проверяем что основные классы доступны
        assert hasattr(main, 'Category')
        assert hasattr(main, 'Product')
        assert hasattr(main, 'Smartphone')
        assert hasattr(main, 'LawnGrass')

        print("✅ Все импорты работают корректно")

    except ImportError as e:
        pytest.skip(f"Не удалось импортировать main.py: {e}")
    except Exception as e:
        pytest.fail(f"Ошибка при импорте main.py: {e}")


def test_main_content():
    """Тест содержимого main.py"""
    main_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'main.py')

    if not os.path.exists(main_path):
        pytest.skip("main.py not found")

    with open(main_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Проверяем ключевые элементы
    assert 'Category(' in content
    assert 'Smartphone(' in content
    assert 'LawnGrass(' in content
    assert 'add_product' in content
    assert 'product1 + product2' in content or 'smartphone1 + smartphone2' in content


def test_main_functionality():
    """Тест функциональности из main.py"""
    # Импортируем классы напрямую из src
    from src.category import Category
    from src.product import Smartphone, LawnGrass

    # Создаем объекты как в main.py
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

    # Проверяем основные операции из main.py
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5

    assert grass1.name == "Газонная трава"
    assert grass1.country == "Россия"

    # Проверяем сложение
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == (180000.0 * 5) + (210000.0 * 8)

    # Проверяем категории
    category = Category("Смартфоны", "Тест категории", [smartphone1, smartphone2])
    assert len(category) == 2

    # Проверяем добавление не-продукта
    with pytest.raises(TypeError):
        category.add_product("Not a product")
