import unittest
from utils.Category import Category
from utils.Product import Product


class TestCategoryInitialization(unittest.TestCase):
    def test_category_initialization(self):
        # Создаем тестовые данные
        name = "Makeup"
        description = "Beauty products"

        # Создаем объект класса Category
        category = Category(name, description)

        # Проверяем корректность инициализации объекта
        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)
        self.assertEqual(category.formatted_products, [])  # Проверяем, что список продуктов пустой

        # Проверяем, что счетчик категорий увеличился
        self.assertEqual(Category.total_categories, 2)

        # Проверяем, что счетчик уникальных продуктов не изменился
        self.assertEqual(Category.unique_products, 0)

    def test_add_product(self):
        # Создаем тестовые данные
        name = "Makeup"
        description = "Beauty products"
        category = Category(name, description)
        product1 = Product("Foundation", "Evens skin tone", 8.0, 20)
        product2 = Product("Eyeshadow Palette", "Variety of eye colors", 16.0, 10)

        # Добавляем продукты в категорию
        category.add_product(product1)
        category.add_product(product2)

        # Проверяем, что продукты были добавлены
        self.assertEqual(len(category.formatted_products), 2)
        self.assertIn("Foundation", category.formatted_products[0])
        self.assertIn("Eyeshadow Palette", category.formatted_products[1])


if __name__ == '__main__':
    unittest.main()
