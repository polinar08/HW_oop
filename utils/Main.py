from Category import Category
from Product import Product
import json


def load_data():
    # Загружаем данные из файла products.json
    with open("products.json", "r") as file:
        data = json.load(file)
    return data


def main():
    data = load_data()  # Загрузка данных
    categories = []

    # Обработка данных и создание экземпляров классов Category и Product
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                product_data["name"],
                product_data["description"],
                product_data["price"],
                product_data["quantity"]
            )
            products.append(product)

        category = Category(
            category_data["name"],
            category_data["description"],
            products
        )
        categories.append(category)

    # Вывод информации о категориях и продуктах
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print("Продукты:")
        for product in category.products:
            print(f"\tПродукт: {product.name}")
            print(f"\tОписание: {product.description}")
            print(f"\tЦена: {product.price}")
            print(f"\tКоличество: {product.quantity_available}")
            print()
        print()


if __name__ == "__main__":
    main()
