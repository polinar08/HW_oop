class Product:
    """Class representing a product."""

    def __init__(self, name, description, price, quantity_available):
        self.name = name  # название продукта
        self.description = description  # описание продукта
        self.__price = price  # цена продукта (приватный атрибут)
        self.quantity_available = quantity_available  # количество товара в наличии

    @property
    def price(self):
        """Геттер для получения цены товара."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для установки цены товара."""
        if value > 0:
            # Проверяем, если цена понижается, запрашиваем подтверждение пользователя
            if value < self.__price:
                confirm = input("Вы уверены, что хотите понизить цену? (y/n): ")
                if confirm.lower() != 'y':
                    print("Действие отменено.")
                    return
            self.__price = value
        else:
            print("Цена введена некорректно.")
