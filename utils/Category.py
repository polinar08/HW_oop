class Category:
    """Класс категории."""

    total_categories = 0  # атрибут для отслеживания общего количества категорий
    total_products = 0  # атрибут для отслеживания общего количества продуктов

    def __init__(self, name, description):
        self.name = name  # название категории
        self.description = description  # описание категории
        self.products = []  # список для хранения товаров

    def add_product(self, product):
        """Метод для добавления товара в категорию."""
        self.products.append(product)
        Category.total_products += 1  # увеличиваем общее количество продуктов

    def __len__(self):
        """Метод для получения количества продуктов в категории."""
        return len(self.products)

    def __str__(self):
        """Метод для строкового представления категории."""
        return f"{self.name}, количество продуктов: {len(self)} шт."