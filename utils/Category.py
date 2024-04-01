from abc import ABC, abstractmethod


class ZeroQuantityError(Exception):
    """Пользовательское исключение для обработки попыток добавить продукт с нулевым количеством."""

    def __init__(self, message="Нельзя добавить продукт с нулевым количеством"):
        self.message = message
        super().__init__(self.message)


class AbstractEntity(ABC):
    def __init__(self, name):
        self.name = name
        print(f"Создан объект {self.__class__.__name__} с именем '{self.name}'.")

    @abstractmethod
    def show_info(self):
        """Абстрактный метод для отображения информации об объекте."""
        pass


class Product:
    def __init__(self, name, description, price, quantity_available):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_available = quantity_available
        print(f"Создан продукт: {self}")

    def __str__(self):
        return f"{self.name}, {self.price} руб. В наличии: {self.quantity_available} шт."


class Category(AbstractEntity):
    total_categories = 0

    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.products = []
        Category.total_categories += 1
        print(f"Создана категория: {self}")

    def add_product(self, product):
        """Добавление продукта в категорию."""
        if isinstance(product, Product):
            if product.quantity_available <= 0:
                raise ZeroQuantityError("Количество продукта нулевое или меньше; нельзя добавить в категорию.")
            self.products.append(product)
            print("Продукт успешно добавлен.")
        else:
            raise TypeError("Можно добавлять только экземпляры продуктов.")
        print("Обработка добавления продукта завершена.")

    def calculate_average_price(self):
        """Расчет средней цены всех продуктов в категории."""
        try:
            total_price = sum([product.price for product in self.products])
            average_price = total_price / len(self.products) if self.products else 0
        except ZeroDivisionError:
            return 0
        return average_price

    def show_info(self):
        """Отображение информации о категории."""
        print(f"Категория: {self.name}")
        print(f"Описание: {self.description}")
        print("Продукты:")
        for product in self.products:
            print(product)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."


class Order(AbstractEntity):
    def __init__(self, product, quantity):
        super().__init__(product.name)
        self.product = product
        self.quantity = quantity
        if quantity <= 0:
            raise ZeroQuantityError("Нельзя создать заказ с количеством нулевым или меньше.")
        self.total_price = product.price * quantity
        print(f"Создан заказ: {self}")

    def show_info(self):
        """Отображение информации о заказе."""
        print(f"Заказ: {self.product.name}")
        print(f"Количество: {self.quantity}")
        print(f"Итоговая стоимость: {self.total_price} руб.")

    def __str__(self):
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб."
