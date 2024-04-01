import unittest
from utils.Category import Category
from utils.Product import Product
from utils.Category import ZeroQuantityError


class TestCategoryInitialization(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        Category.total_categories = 0  # Сброс общего количества категорий

    def test_category_initialization(self):
        # Создаем тестовые данные
        name = "Makeup"
        description = "Beauty products"

        # Создаем объект класса Category
        category = Category(name, description)

        # Проверяем корректность инициализации объекта
        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)
        self.assertEqual(len(category.products), 0)
        self.assertEqual(Category.total_categories, 1)

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

        # Проверяем, что продукты добавлены
        self.assertIn(product1, category.products)
        self.assertIn(product2, category.products)


class TestCategoryFeatures(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        Category.total_categories = 0
        self.category = Category("Makeup", "Beauty products")

    def test_add_zero_quantity_product(self):
        """Тест на невозможность добавления продукта с нулевым количеством."""
        with self.assertRaises(ZeroQuantityError):
            self.category.add_product(Product("Lip Gloss", "Shiny lip gloss", 10.0, 0))

    def test_calculate_average_price(self):
        """Тест расчета средней цены продуктов в категории."""
        product1 = Product("Foundation", "Evens skin tone", 20.0, 10)
        product2 = Product("Eyeshadow Palette", "Variety of eye colors", 40.0, 5)
        self.category.add_product(product1)
        self.category.add_product(product2)
        expected_average_price = (product1.price + product2.price) / 2
        self.assertEqual(self.category.calculate_average_price(), expected_average_price)

    def test_calculate_average_price_empty_category(self):
        """Тест расчета средней цены при отсутствии продуктов в категории."""
        self.assertEqual(self.category.calculate_average_price(), 0)


if __name__ == '__main__':
    unittest.main()
