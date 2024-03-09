from abc import ABC, abstractmethod


class LoggingMixin:
    """Миксин для логирования информации о созданных объектах."""

    def __repr__(self):
        """Метод для вывода информации о созданном объекте."""
        class_name = self.__class__.__name__  # Получаем название класса
        attributes = ', '.join([f"{attr}={getattr(self, attr)}" for attr in self.__dict__])  # Получаем атрибуты объекта
        return f"{class_name}({attributes})"


class AbstractProduct(ABC, LoggingMixin):
    """Абстрактный базовый класс для всех классов продуктов."""

    def __init__(self, name, description, price, quantity_available):
        """Инициализация абстрактного продукта."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_available = quantity_available

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


class Product(AbstractProduct):
    """Класс, представляющий общий продукт."""

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


class Smartphone(AbstractProduct):
    """Класс, представляющий смартфон."""

    def __init__(self, name, description, price, quantity_available, performance, model, memory, color):
        super().__init__(name, description, price, quantity_available)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод для сложения двух смартфонов."""
        if isinstance(other, self.__class__):
            return self.calculate_total_price() + other.calculate_total_price()
        else:
            raise ValueError("Нельзя сложить смартфон с объектом другого типа.")

    def get_details(self):
        """Метод для получения деталей продукта."""
        return f"{self.name}, {self.description}, {self.price}, {self.quantity_available}, {self.performance}, {self.model}, {self.memory}, {self.color}"

    def calculate_total_price(self):
        """Метод для вычисления общей стоимости продукта."""
        return self.price * self.quantity_available


class LawnGrass(AbstractProduct):
    """Класс, представляющий газонную траву."""

    def __init__(self, name, description, price, quantity_available, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity_available)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод для сложения двух газонных трав."""
        if isinstance(other, self.__class__):
            return self.calculate_total_price() + other.calculate_total_price()
        else:
            raise ValueError("Нельзя сложить газонную траву с объектом другого типа.")

    def get_details(self):
        """Метод для получения деталей продукта."""
        return f"{self.name}, {self.description}, {self.price}, {self.quantity_available}, {self.country_of_origin}, {self.germination_period}, {self.color}"

    def calculate_total_price(self):
        """Метод для вычисления общей стоимости продукта."""
        return self.price * self.quantity_available