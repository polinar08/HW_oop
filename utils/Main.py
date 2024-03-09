from utils.Product import Product, Smartphone, LawnGrass
from utils.Category import Category
import json


def load_data():
    # Загрузка данных из файла "products.json"
    with open("products.json", "r") as file:
        data = json.load(file)
    return data


def main():
    data = load_data()  # Загрузка данных
    categories = []  # Создание списка категорий

    # Обработка данных и создание экземпляров классов Category и продуктов
    for category_data in data:
        category = Category(category_data["name"], category_data["description"])
        categories.append(category)  # Добавление категории в список категорий

        # Добавление продуктов в категорию
        for product_data in category_data["products"]:
            if product_data['type'] == "product":
                product = Product(
                    product_data["name"],
                    product_data["description"],
                    product_data["price"],
                    product_data["quantity"]
                )
            elif product_data["type"] == "smartphone":
                product = Smartphone(
                    product_data["name"],
                    product_data["description"],
                    product_data["price"],
                    product_data["quantity"],
                    product_data["performance"],
                    product_data["model"],
                    product_data["memory"],
                    product_data["color"]
                )
            elif product_data["type"] == "lawn_grass":
                product = LawnGrass(
                    product_data["name"],
                    product_data["description"],
                    product_data["price"],
                    product_data["quantity"],
                    product_data["country_of_origin"],
                    product_data["germination_period"],
                    product_data["color"]
                )
            else:
                raise ValueError("Unknown product type.")

            category.add_product(product)  # Добавление продукта в категорию

    # Вывод информации о категориях и продуктах
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print("Продукты:")
        for product in category.products:
            print(product)  # Вывод информации о продукте
        print()


if __name__ == "__main__":
    main()
