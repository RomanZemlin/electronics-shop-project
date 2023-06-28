import csv
import math
import os

from exceptions.InstantiateCSV import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        try:
            items = os.path.join(os.path.dirname(__file__), 'items.csv')

            with open(items, 'r', encoding='windows-1251') as f:
                data = csv.reader(f, delimiter=' ')
                item = []
                for i in data:
                    item.append(i)
                for i in item[1:]:
                    data = i[0].split(',')
                    Item(data[0], data[1], data[2])

        except InstantiateCSVError as error:
            print(error)
        except FileNotFoundError:
            print("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(number: str):
        return math.floor(float(number))
