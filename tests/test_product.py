import io
import sys

import pytest

from src.product import BaseProduct, LawnGrass, Product, Smartphone, ZeroQuantityError


def test_base_product_is_abstract() -> None:
    """Проверка, что BaseProduct нельзя инстанциировать"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100, 1)  # type: ignore


def test_product_logging(capsys) -> None:  # type: ignore
    """Проверка логирования создания Product"""
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.name == "Test Product"
    captured = capsys.readouterr()
    assert "Product('Test Product', 'Description', 100.0, 10)" in captured.out


def test_smartphone_logging_all_parameters(capsys) -> None:  # type: ignore
    """Проверка что Smartphone выводит все 8 параметров"""
    smartphone = Smartphone("Phone", "Desc", 100.0, 5, 2.0, "Model", 128, "Black")
    assert smartphone.name == "Phone"
    captured = capsys.readouterr()
    output = captured.out

    # Проверяем что выведены все 8 параметров
    assert "Smartphone(" in output
    # Должно быть 7 запятых для 8 параметров
    assert output.count(",") == 7
    # Проверяем наличие всех параметров
    assert "'Phone'" in output
    assert "100.0" in output
    assert "2.0" in output
    assert "'Model'" in output
    assert "128" in output
    assert "'Black'" in output


def test_lawn_grass_logging_all_parameters(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверка что LawnGrass выводит все 7 параметров"""
    grass = LawnGrass("Grass", "Green grass", 50.0, 20, "Russia", "14 days", "Green")
    captured = capsys.readouterr()
    output = captured.out

    assert "LawnGrass(" in output
    assert output.count(",") == 6  # 6 запятых для 7 параметров
    assert "'Russia'" in output
    assert "'14 days'" in output
    assert "'Green'" in output
    assert grass.country == "Russia"


def test_product_inheritance() -> None:
    """Проверка наследования"""
    product = Product("Test", "Test", 100, 1)
    assert isinstance(product, BaseProduct)

    smartphone = Smartphone("Phone", "Desc", 100, 1, 2.0, "M", 128, "B")
    assert isinstance(smartphone, Product)
    assert isinstance(smartphone, BaseProduct)

    # Проверяем что Smartphone наследует только от Product
    assert Smartphone.__bases__ == (Product,)


def test_logmixin_repr() -> None:
    """Проверка метода __repr__ из миксина"""
    product = Product("Test", "Desc", 100, 5)
    assert repr(product) == "Product(name='Test')"

    smartphone = Smartphone("Phone", "Desc", 100, 1, 2.0, "M", 128, "B")
    assert repr(smartphone) == "Smartphone(name='Phone')"


def test_product_addition() -> None:
    """Проверка сложения продуктов"""
    p1 = Product("P1", "Desc", 100, 2)
    p2 = Product("P2", "Desc", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3

    s1 = Smartphone("S1", "Desc", 100, 2, 2.0, "M", 128, "B")
    s2 = Smartphone("S2", "Desc", 200, 3, 2.0, "M", 128, "B")
    assert s1 + s2 == 100 * 2 + 200 * 3


def test_addition_different_types() -> None:
    """Проверка ошибки при сложении разных типов"""
    smartphone = Smartphone("Phone", "Desc", 100, 1, 2.0, "M", 128, "B")
    grass = LawnGrass("Grass", "Desc", 50, 2, "R", "14", "G")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
        smartphone + grass


def test_product_price_property() -> None:
    """Проверка property price"""
    product = Product("Test", "Desc", 100, 5)
    assert product.price == 100

    # Изменение цены
    product.price = 150
    assert product.price == 150

    # Проверка на отрицательную цену
    captured_output = io.StringIO()
    sys.stdout = captured_output
    product.price = -10
    sys.stdout = sys.__stdout__
    assert "Цена не должна быть нулевой или отрицательной" in captured_output.getvalue()
    assert product.price == 150  # Цена не изменилась


# tests/test_product.py (добавить в конец)


def test_zero_quantity_in_product_creation(capsys: pytest.CaptureFixture[str]):  # type: ignore
    """Тест создания продукта с нулевым количеством"""
    with pytest.raises(ZeroQuantityError):  # type: ignore
        Product("Test", "Desc", 100.0, 0)

    # Проверяем что не было попытки логирования
    captured = capsys.readouterr()
    assert "Product(" not in captured.out
