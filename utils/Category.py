from abc import ABC, abstractmethod


class AbstractEntity(ABC):
    """Абстрактный базовый класс для классов Order и Category."""

    def __init__(self, name):
        """Инициализация абстрактного объекта с именем."""
        self.name = name
        print(f"Создан объект {self.__class__.__name__} с именем '{self.name}'.")

    @abstractmethod
    def show_info(self):
        """Абстрактный метод для отображения информации об объекте."""
        pass


class Product:
    """Класс, представляющий продукт."""

    def __init__(self, name, description, price, quantity_available):
        """Инициализация продукта с названием, описанием, ценой и доступным количеством."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_available = quantity_available
        print(f"Создан продукт: {self}")

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. В наличии: {self.quantity_available} шт."


class Category(AbstractEntity):
    """Класс, представляющий категорию продуктов."""

    total_categories = 0  # Атрибут для отслеживания общего количества категорий

    def __init__(self, name, description):
        """Инициализация категории с названием и описанием."""
        super().__init__(name)
        self.description = description
        self.products = []
        Category.total_categories += 1
        print(f"Создана категория: {self}")

    def add_product(self, product):
        """Добавление продукта в категорию."""
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Можно добавить только продукт.")

    def show_info(self):
        """Отображение информации о категории."""
        print(f"Категория: {self.name}")
        print(f"Описание: {self.description}")
        print("Продукты:")
        for product in self.products:
            print(product)

    def __str__(self):
        """Возвращает строковое представление категории."""
        return f"{self.name}, количество продуктов: {len(self.products)} шт."


class Order(AbstractEntity):
    """Класс, представляющий заказ."""

    def __init__(self, product, quantity):
        """Инициализация заказа с продуктом и его количеством."""
        super().__init__(product.name)
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity
        print(f"Создан заказ: {self}")

    def show_info(self):
        """Отображение информации о заказе."""
        print(f"Заказ: {self.product.name}")
        print(f"Количество: {self.quantity}")
        print(f"Итоговая стоимость: {self.total_price} руб.")

    def __str__(self):
        """Возвращает строковое представление заказа."""
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб."