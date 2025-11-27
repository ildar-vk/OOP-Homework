class TestProductAddition:
    """Тесты для сложения продуктов"""

    def test_smartphone_addition_same_type(self):
        """Тест сложения смартфонов одного типа"""
        phone1 = Smartphone("Phone1", "Desc", 1000.0, 2, 95.5, "Model1", 128, "Black")
        phone2 = Smartphone("Phone2", "Desc", 1500.0, 3, 98.2, "Model2", 256, "White")

        result = phone1 + phone2
        expected = (1000.0 * 2) + (1500.0 * 3)  # 2000 + 4500 = 6500
        assert result == expected

    def test_lawn_grass_addition_same_type(self):
        """Тест сложения газонных трав одного типа"""
        grass1 = LawnGrass("Grass1", "Desc", 300.0, 5, "Russia", "7 days", "Green")
        grass2 = LawnGrass("Grass2", "Desc", 400.0, 3, "USA", "5 days", "Dark Green")

        result = grass1 + grass2
        expected = (300.0 * 5) + (400.0 * 3)  # 1500 + 1200 = 2700
        assert result == expected

    def test_product_addition_same_type(self):
        """Тест сложения обычных продуктов одного типа"""
        product1 = Product("Product1", "Desc", 100.0, 4)
        product2 = Product("Product2", "Desc", 200.0, 2)

        result = product1 + product2
        expected = (100.0 * 4) + (200.0 * 2)  # 400 + 400 = 800
        assert result == expected

    def test_smartphone_lawn_grass_addition_error(self):
        """Тест ошибки при сложении смартфона и газонной травы"""
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "Russia", "7 days", "Green")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            phone + grass

    def test_product_smartphone_addition_error(self):
        """Тест ошибки при сложении обычного продукта и смартфона"""
        product = Product("Product", "Desc", 100.0, 4)
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            product + phone

    def test_product_lawn_grass_addition_error(self):
        """Тест ошибки при сложении обычного продукта и газонной травы"""
        product = Product("Product", "Desc", 100.0, 4)
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "Russia", "7 days", "Green")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            product + grass

    def test_smartphone_product_addition_error(self):
        """Тест ошибки при сложении смартфона и обычного продукта"""
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.5, "Model", 128, "Black")
        product = Product("Product", "Desc", 100.0, 4)

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            phone + product

    def test_lawn_grass_product_addition_error(self):
        """Тест ошибки при сложении газонной травы и обычного продукта"""
        grass = LawnGrass("Grass", "Desc", 300.0, 5, "Russia", "7 days", "Green")
        product = Product("Product", "Desc", 100.0, 4)

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            grass + product