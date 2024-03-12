from abc import ABC, abstractmethod


class LoggingMixin:
    """Миксин для логирования информации о созданных объектах."""

    def __init__(self, *args):
        """Инициализация объекта и вывод информации о нем."""
        print(repr(self))

    def __repr__(self):
        """Возвращает строковое представление объекта."""
        object_attributes = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f"создан объект со свойствами: ({object_attributes})"


class AbstractProduct(ABC):
    """Абстрактный базовый класс для всех классов продуктов."""

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод для сложения двух продуктов."""
        pass

    @abstractmethod
    def get_details(self):
        """Абстрактный метод для получения деталей продукта."""
        pass

    @abstractmethod
    def calculate_total_price(self):
        """Абстрактный метод для вычисления общей стоимости продукта."""
        pass

    @abstractmethod
    def new_product(cls, product_data: dict):
        """Абстрактный классовый метод для создания нового продукта."""
        pass

    new_product = classmethod(new_product)


class Product(AbstractProduct, LoggingMixin):
    """Класс, представляющий общий продукт."""

    def __init__(self, name, description, price, quantity_available):
        """Инициализация продукта."""
        super().__init__()
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

    @classmethod
    def new_product(cls, product_data: dict):
        """Классовый метод для создания нового продукта."""
        return cls(**product_data)


# Примеры подклассов, которые могут использовать метод new_product

class Smartphone(Product):
    """Класс, представляющий смартфон."""

    def __init__(self, name, description, price, quantity_available, performance, model, memory, color):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity_available)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def get_details(self):
        """Метод для получения деталей продукта."""
        return (f"{self.name}, {self.description}, {self.price}, {self.quantity_available}, {self.performance},"
                f" {self.model}, {self.memory}, {self.color}")


class LawnGrass(Product):
    """Класс, представляющий газонную траву."""

    def __init__(self, name, description, price, quantity_available, country_of_origin, germination_period, color):
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity_available)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def get_details(self):
        """Метод для получения деталей продукта."""
        return (f"{self.name}, {self.description}, {self.price}, {self.quantity_available}, {self.country_of_origin}, "
                f"{self.germination_period}, {self.color}")