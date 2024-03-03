class Product:
    """Класс представляющий продукт."""

    def __init__(self, name, description, price, quantity_available):
        self.name = name  # название продукта
        self.description = description  # описание продукта
        self.price = price  # цена продукта
        self.quantity_available = quantity_available  # количество товара в наличии

    @property
    def price(self):
        """Геттер для получения цены товара."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для установки цены товара."""
        if value > 0:
            self.__price = value
        else:
            print("Цена введена некорректно.")

    def __add__(self, other):
        """Метод для операции сложения двух продуктов."""
        if isinstance(other, Product):
            total_price_self = self.price * self.quantity_available
            total_price_other = other.price * other.quantity_available
            return total_price_self + total_price_other
        else:
            raise ValueError("Нельзя сложить продукт с объектом другого типа.")

    def __str__(self):
        """Метод для строкового представления продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_available} шт."


class Smartphone(Product):
    """Подкласс для представления смартфонов."""

    def __init__(self, name, description, price, quantity_available, performance, model, memory, color):
        super().__init__(name, description, price, quantity_available)
        self.performance = performance  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет


class LawnGrass(Product):
    """Подкласс для представления газонной травы."""

    def __init__(self, name, description, price, quantity_available, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity_available)
        self.country_of_origin = country_of_origin  # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет