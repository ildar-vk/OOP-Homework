# main.py

from src.category import Category
from src.product import Product, Smartphone, LawnGrass, ZeroQuantityError

if __name__ == "__main__":
    print("=== Тестирование обработки исключений ===")

    # Тест 1: Создание товара с нулевым количеством (Задание 1)
    print("\n1. Тест создания товара с нулевым количеством:")
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        print("ОШИБКА: Исключение не было вызвано!")
    except ZeroQuantityError as e:
        print(f"✅ Корректно вызвано исключение: {e}")
    except ValueError as e:
        print(f"✅ Вызвано исключение ValueError: {e}")

    # Тест 2: Создание корректных товаров
    print("\n2. Создание корректных товаров:")
    try:
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        print("✅ Товары созданы успешно")
    except ZeroQuantityError as e:
        print(f"ОШИБКА: {e}")

    # Тест 3: Расчет среднего ценника (Задание 2)
    print("\n3. Расчет среднего ценника категории:")
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    average_price = category1.middle_price()
    print(f"Средний ценник в категории '{category1.name}': {average_price:.2f} руб.")

    # Тест 4: Расчет среднего ценника для пустой категории
    print("\n4. Расчет среднего ценника для пустой категории:")
    category_empty = Category("Пустая категория", "Категория без продуктов", [])

    average_empty = category_empty.middle_price()
    print(f"Средний ценник в пустой категории: {average_empty} руб.")
    print("✅ Обработано деление на ноль, возвращен 0")

    # Тест 5: Дополнительное задание - полный обработчик
    print("\n5. Дополнительное задание - полная обработка:")
    print("Попытка добавления товара в категорию:")

    try:
        # Пробуем создать товар с нулевым количеством
        bad_product = Product("Пробный товар", "Описание", 500.0, 0)
        category_empty.add_product(bad_product)

    except ZeroQuantityError as e:
        print(f"❌ Исключение при создании товара: {e}")
    except Exception as e:
        print(f"❌ Произошла ошибка: {type(e).__name__}: {e}")
    else:
        print("✅ Товар успешно добавлен в категорию")
    finally:
        print("ℹ️ Обработка добавления товара завершена")

    print("\n=== Тестирование завершено ===")