class Category:
    """Класс категории."""

    total_categories = 0  # атрибут для отслеживания общего количества категорий
    unique_products = 0  # атрибут для отслеживания общего количества уникальных продуктов

    def __init__(self, name, description):
        self.name = name  # название категории
        self.description = description  # описание категории
        self.__products = []  # приватный атрибут для хранения товаров
        Category.total_categories += 1  # увеличиваем общее количество категорий

    def add_product(self, product):
        """Метод для добавления товара в категорию."""
        self.__products.append(product)

    @property
    def products(self):
        """Геттер для получения списка товаров в категории."""
        return self.__products

    @property
    def formatted_products(self):
        """Геттер для вывода списка товаров в формате."""
        formatted_list = []
        for product in self.__products:
            formatted_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity_available} шт.")
        return formatted_list