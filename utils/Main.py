from Category import Category
from Product import Product
import json


def load_data():
    # Загрузка данных из файла "products.json"
    with open("products.json", "r") as file:
        data = json.load(file)
    return data


def main():
    data = load_data()  # Загрузка данных
    categories = []  # Создание списка категорий

    # Обработка данных и создание экземпляров классов Category и Product
    for category_data in data:
        category = Category(category_data["name"], category_data[
            "description"])  # Создание экземпляра класса Category без передачи списка товаров
        categories.append(category)  # Добавление категории в список категорий

        # Добавление товаров в категорию
        for product_data in category_data["products"]:
            product = Product(
                product_data["name"],
                product_data["description"],
                product_data["price"],
                product_data["quantity"]
            )
            category.add_product(product)  # Добавление товара в категорию с помощью метода add_product()

    # Вывод информации о категориях и продуктах
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print("Продукты:")
        for product in category.formatted_products:  # Используем геттер formatted_products для вывода товаров
            print(product)
        print()


if __name__ == "__main__":
    main()
