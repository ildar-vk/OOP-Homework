# tests/test_exceptions.py

import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone, ZeroQuantityError


class TestExceptionsHomework:
    """Тесты для ДЗ 17.1: Исключения"""

    def test_zero_quantity_raises_exception(self) -> None:
        """Задание 1: Товар с quantity=0 вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            Product("Тестовый товар", "Описание", 100.0, 0)

        assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
        assert isinstance(exc_info.value, ZeroQuantityError)

    def test_zero_quantity_custom_exception_message(self) -> None:
        """Проверка сообщения пользовательского исключения"""
        try:
            Product("Товар", "Описание", 50.0, 0)
        except ZeroQuantityError as e:
            assert e.message == "Товар с нулевым количеством не может быть добавлен"
            assert str(e) == "Товар с нулевым количеством не может быть добавлен"

    def test_valid_product_creation(self) -> None:
        """Создание товара с положительным количеством работает"""
        product = Product("Валидный товар", "Описание", 100.0, 5)
        assert product.name == "Валидный товар"
        assert product.quantity == 5
        assert product.price == 100.0

    def test_middle_price_calculation(self) -> None:
        """Задание 2: Расчет среднего ценника с товарами"""
        product1 = Product("Товар 1", "Описание", 100.0, 2)
        product2 = Product("Товар 2", "Описание", 200.0, 3)
        product3 = Product("Товар 3", "Описание", 300.0, 1)

        category = Category("Тестовая", "Описание", [product1, product2, product3])
        result = category.middle_price()

        # (100 + 200 + 300) / 3 = 200
        assert result == 200.0
        assert isinstance(result, float)

    def test_middle_price_empty_category(self) -> None:
        """Задание 2: Пустая категория возвращает 0"""
        category = Category("Пустая", "Описание", [])
        result = category.middle_price()

        assert result == 0.0
        assert isinstance(result, float)

    def test_middle_price_single_product(self) -> None:
        """Средний ценник для одного товара"""
        product = Product("Один товар", "Описание", 150.0, 1)
        category = Category("Один", "Описание", [product])

        assert category.middle_price() == 150.0

    def test_middle_price_after_adding_products(self) -> None:
        """Средний ценник после добавления товаров"""
        category = Category("Динамическая", "Описание", [])
        assert category.middle_price() == 0.0

        product1 = Product("Товар 1", "Описание", 100.0, 2)
        category.add_product(product1)
        assert category.middle_price() == 100.0

        product2 = Product("Товар 2", "Описание", 200.0, 3)
        category.add_product(product2)
        assert category.middle_price() == 150.0

    def test_inherited_classes_zero_quantity(self) -> None:
        """Наследники Product тоже должны вызывать исключение"""
        with pytest.raises(ZeroQuantityError):
            Smartphone("Смартфон", "Описание", 1000.0, 0, 95.5, "Model", 128, "Black")

        with pytest.raises(ZeroQuantityError):
            LawnGrass("Трава", "Описание", 500.0, 0, "Россия", "14 дней", "Зеленый")

    def test_try_except_else_finally_pattern(self) -> None:
        """Дополнительное задание: полный паттерн try/except/else/finally"""
        execution_log = []

        try:
            # Пытаемся создать товар с нулевым количеством
            product = Product("Тест", "Описание", 100.0, 0)
            execution_log.append("Товар создан")
            category = Category("Тест", "Описание", [])
            category.add_product(product)
            execution_log.append("Товар добавлен")
        except ZeroQuantityError as e:
            execution_log.append(f"Поймано исключение: {e}")
        except Exception as e:
            execution_log.append(f"Другое исключение: {type(e).__name__}")
        else:
            execution_log.append("Блок else выполнен")
        finally:
            execution_log.append("Блок finally выполнен")

        # Проверяем порядок выполнения
        assert len(execution_log) == 2
        assert "Поймано исключение" in execution_log[0]
        assert "Блок finally выполнен" in execution_log[1]
        assert "Блок else выполнен" not in execution_log

    def test_try_except_else_finally_success_case(self) -> None:
        """Паттерн try/except/else/finally для успешного случая"""
        execution_log = []

        try:
            product = Product("Тест", "Описание", 100.0, 5)
            execution_log.append("Товар создан")
            category = Category("Тест", "Описание", [])
            category.add_product(product)
            execution_log.append("Товар добавлен")
        except ZeroQuantityError as e:
            execution_log.append(f"Поймано исключение: {e}")
        except Exception as e:
            execution_log.append(f"Другое исключение: {type(e).__name__}")
        else:
            execution_log.append("Блок else: успешно")
        finally:
            execution_log.append("Блок finally: завершено")

        # Проверяем порядок выполнения
        assert len(execution_log) == 4
        assert "Товар создан" in execution_log[0]
        assert "Товар добавлен" in execution_log[1]
        assert "Блок else: успешно" in execution_log[2]
        assert "Блок finally: завершено" in execution_log[3]


def test_category_methods_still_work() -> None:
    """Проверка что старые методы категории все еще работают"""
    product = Product("Тест", "Описание", 100.0, 5)
    category = Category("Тест", "Описание", [product])

    # Старые методы должны работать
    assert len(category) == 1
    assert str(category) == "Тест, количество продуктов: 5 шт."
    assert "Тест, 100.0 руб. Остаток: 5 шт." in category.products
    assert category.products_list == [product]


def test_product_methods_still_work() -> None:
    """Проверка что старые методы продукта все еще работают"""
    product1 = Product("Товар 1", "Описание", 100.0, 2)
    product2 = Product("Товар 2", "Описание", 200.0, 3)

    # Сложение должно работать
    total = product1 + product2
    assert total == 100.0 * 2 + 200.0 * 3

    # Изменение цены должно работать
    product1.price = 150.0
    assert product1.price == 150.0
