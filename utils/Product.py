class Product:
    """Class representing a product."""

    def __init__(self, name, description, price, quantity_available):
        self.name = name  # название продукта
        self.description = description  # описание продукта
        self.price = price  # цена продукта
        self.quantity_available = quantity_available  # количество товара в наличии

    @classmethod
    def create(cls, name, description, price, quantity_available, product_list=None):
        """Метод для создания нового товара и проверки наличия дубликата."""
        if product_list:
            for existing_product in product_list:
                if existing_product.name == name:
                    # Если товар уже существует, обновляем количество в наличии и цену
                    existing_product.quantity_available += quantity_available
                    existing_product.price = max(existing_product.price, price)
                    return existing_product
        # Если товар не найден или список товаров пуст, создаем новый объект товара
        return cls(name, description, price, quantity_available)
