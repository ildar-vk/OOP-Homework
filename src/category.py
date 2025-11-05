class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        # name: str
        # description: str
        # category_count: int
        # product_count: int
        # products: list

        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
