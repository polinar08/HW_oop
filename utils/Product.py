from abc import ABC, abstractmethod


class PrintMixin:
    """Миксин для вывода информации о созданных объектах."""

    def __repr__(self):
        """Метод для представления объекта в виде строки."""
        object_attributes = ', '.join([f'{k}: {v}' for k, v in self.__dict__.items()])
        return f"создан объект со свойствами {object_attributes})"


class AbstractProduct(ABC):
    """Абстрактный базовый класс для всех классов продуктов."""

    @abstractmethod
    def __add__(self, other):
        """Метод для сложения двух продуктов."""
        pass

    @abstractmethod
    def get_details(self):
        """Метод для получения деталей продукта."""
        pass

    @abstractmethod
    def calculate_total_price(self):
        """Метод для вычисления общей стоимости продукта."""
        pass


class Product(AbstractProduct, PrintMixin):
    """Класс, представляющий общий продукт."""

    def __init__(self, name, description, price, quantity_available):
        """Инициализация продукта."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_available = quantity_available

    def __add__(self, other):
        """Метод для сложения двух продуктов."""
        if isinstance(other, self.__class__):
            return self.calculate_total_price() + other.calculate_total_price()
        else:
            raise ValueError("Нельзя сложить продукт с объектом другого типа.")

    def get_details(self):
        """Метод для получения деталей продукта."""
        return f"{self.name}, {self.description}, {self.price}, {self.quantity_available}"

    def calculate_total_price(self):
        """Метод для вычисления общей стоимости продукта."""
        return self.price * self.quantity_available


class Smartphone(Product):
    """Класс, представляющий смартфон."""

    def __init__(self, name, description, price, quantity_available, performance, model, memory, color):
        super().__init__(name, description, price, quantity_available)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс, представляющий газонную траву."""

    def __init__(self, name, description, price, quantity_available, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity_available)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color