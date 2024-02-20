import unittest
from utils.Category import Category


class TestCategoryInitialization(unittest.TestCase):
    def test_category_initialization(self):
        # Создаем тестовые данные
        name = "Makeup"
        description = "Beauty products"
        products = []

        # Создаем объект класса Category
        category = Category(name, description, products)

        # Проверяем корректность инициализации объекта
        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)
        self.assertEqual(category.products, products)
        self.assertEqual(Category.total_categories, 1)  # Проверяем увеличение счетчика категорий
        self.assertEqual(Category.unique_products, 0)  # Проверяем, что счетчик уникальных продуктов не изменился


if __name__ == '__main__':
    unittest.main()
