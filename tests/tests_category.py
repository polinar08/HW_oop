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
        self.assertEqual(category.name, name)  # Проверяем, что имя категории установлено правильно
        self.assertEqual(category.description, description)  # Проверяем, что описание категории установлено правильно
        self.assertEqual(len(category.products), 0)  # Проверяем, что список продуктов пустой

        # Проверяем, что счетчик категорий увеличился
        self.assertEqual(Category.total_categories, 0)

        # Проверяем, что счетчик уникальных продуктов не изменился
        self.assertEqual(Category.total_products, 2)

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
        self.assertEqual(len(category.products), 2)  # Проверяем, что количество продуктов в категории равно 2
        self.assertIn("Foundation", [product.name for product in category.products])  # Проверяем наличие продукта
        # "Foundation"
        self.assertIn("Eyeshadow Palette", [product.name for product in category.products])  # Проверяем наличие
        # продукта "Eyeshadow Palette"


if __name__ == '__main__':
    unittest.main()