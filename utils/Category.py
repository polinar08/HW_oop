class Category:
    """Класс категории."""
    total_categories = 0  # атрибут для отслеживания общего количества категорий
    unique_products = 0  # атрибут для отслеживания общего количества уникальных продуктов

    def __init__(self, name, description, products):
        self.name = name  # название категории
        self.description = description  # описание категории
        self.products = products  # товары в категории
        Category.total_categories += 1  # увеличиваем общее количество категорий
        Category.unique_products += len(products)  # увеличиваем общее количество уникальных продуктов
