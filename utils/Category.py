class Category:
    """Class representing a category of products."""
    total_categories = 0
    unique_products = 0

    def __init__(self, name, description, products):
        self.name = name  # название категории
        self.description = description  # описание категории
        self.products = products  # товары в категории
        Category.total_categories += 1
        Category.unique_products += len(products)