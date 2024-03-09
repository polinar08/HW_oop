import unittest
from utils.Category import Category
from utils.Product import Product


class TestCategoryInitialization(unittest.TestCase):
    def test_category_initialization(self):
        Category.total_categories = 0  # Reset total_categories
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
        self.assertEqual(Category.total_categories, 1)

    def test_add_product(self):
        Category.total_categories = 0  # Reset total_categories
        # Создаем тестовые данные
        name = "Makeup"
        description = "Beauty products"
        category = Category(name, description)
        product1 = Product("Foundation", "Evens skin tone", 8.0, 20)
        product2 = Product("Eyeshadow Palette", "Variety of eye colors", 16.0, 10)

        # Проверяем, что добавление недопустимого типа продукта вызывает TypeError
        with self.assertRaises(TypeError):
            category.add_product("Not a Product instance")

        # Проверяем, что список продуктов не изменился
        self.assertEqual(len(category.products), 0)


if __name__ == '__main__':
    unittest.main()