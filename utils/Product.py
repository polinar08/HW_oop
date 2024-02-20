class Product:
    """Class representing a product."""
    def __init__(self, name, description, price, quantity_available):
        self.name = name  # название продукта
        self.description = description  # описание продукта
        self.price = price  # цена продукта
        self.quantity_available = quantity_available  # количество товара в наличии

