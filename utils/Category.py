class Category:
    """Class representing a category of products."""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для хранения товаров

    def add_product(self, product):
        """Метод для добавления товара в категорию."""
        self.__products.append(product)

    @property
    def products(self):
        """Геттер для получения списка товаров."""
        return self.__products