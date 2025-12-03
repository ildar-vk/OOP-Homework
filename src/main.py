from src.category import Category
from src.product import BaseProduct, LawnGrass, LogMixin, Product, Smartphone

if __name__ == "__main__":
    print("=== Тестирование нового функционала (абстрактные классы и миксины) ===")

    # Тестирование базового продукта с миксином
    print("\n1. Создание обычного продукта (должен быть лог):")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    print("\n2. Создание смартфона (должен быть лог):")
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

    print("\n3. Создание газонной травы (должен быть лог):")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    # Проверка что все работает как раньше
    print("\n4. Проверка функциональности:")
    print(f"Продукт: {product1}")
    print(f"Смартфон: {smartphone1}")
    print(f"Газонная трава: {grass1}")

    # Тестирование __repr__ из миксина
    print("\n5. Проверка __repr__ (из миксина):")
    print(f"repr(product1): {repr(product1)}")
    print(f"repr(smartphone1): {repr(smartphone1)}")
    print(f"repr(grass1): {repr(grass1)}")

    # Проверка наследования
    print("\n6. Проверка наследования:")
    print(f"product1 является BaseProduct: {isinstance(product1, BaseProduct)}")
    print(f"product1 является LogMixin: {isinstance(product1, LogMixin)}")
    print(f"smartphone1 является BaseProduct: {isinstance(smartphone1, BaseProduct)}")
    print(f"grass1 является BaseProduct: {isinstance(grass1, BaseProduct)}")

    # Тестирование MRO (Method Resolution Order)
    print("\n7. Проверка порядка разрешения методов (MRO):")
    print(f"Product MRO: {[cls.__name__ for cls in Product.__mro__]}")
    print(f"Smartphone MRO: {[cls.__name__ for cls in Smartphone.__mro__]}")
    print(f"LawnGrass MRO: {[cls.__name__ for cls in LawnGrass.__mro__]}")

    # Тестирование сложения (старая функциональность должна работать)
    print("\n8. Тестирование сложения:")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone_sum = smartphone1 + smartphone2
    print(f"Сумма смартфонов: {smartphone_sum}")

    # Проверка ошибки при сложении разных типов
    try:
        invalid_sum = smartphone1 + grass1
        print("ОШИБКА: сложение прошло успешно (не должно было)")
    except TypeError as e:
        print(f"✅ Корректная ошибка при сложении разных типов: {e}")

    # Тестирование категорий
    print("\n9. Тестирование категорий:")
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    print(f"Категория: {category_smartphones}")
    print(f"Товары в категории:\n{category_smartphones.products}")

    print("\n=== Тестирование завершено ===")
