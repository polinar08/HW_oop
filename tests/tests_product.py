import unittest
from utils.Product import Product


class TestProductInitialization(unittest.TestCase):
    def test_product_initialization(self):
        # Создаем тестовые данные для продукта
        name = "Foundation"
        description = "Evens skin tone"
        price = 20.0
        quantity_available = 10

        # Создаем объект класса Product
        product = Product(name, description, price, quantity_available)

        # Проверяем корректность инициализации объекта
        self.assertEqual(product.name, name)
        self.assertEqual(product.description, description)
        self.assertEqual(product.price, price)
        self.assertEqual(product.quantity_available, quantity_available)


if __name__ == '__main__':
    unittest.main()
