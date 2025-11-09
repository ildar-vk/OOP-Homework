class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        # name: str
        # description: str
        # price: float
        # quantity: int

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_date):
        name = product_date.get("name")
        description = product_date.get("description")
        price = product_date.get("price")
        quantity = product_date.get("quantity")

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if price <=0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            self.__price = price
