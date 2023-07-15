import csv
import math
import os

from exceptions.exceptions import InstantiateCSVError


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
    def instantiate_from_csv(cls, path_to_file='../src/items.csv'):
        """Загружает из файла .csv данные и создает на их основе экземпляры класса Item"""
        cls.all = []
        try:
            with open(path_to_file, 'r', encoding='CP1251') as csv_file:
                rows = csv.DictReader(csv_file)
                for row in rows:
                    try:
                        cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))
                    except:
                        raise InstantiateCSVError('Файл item.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(number: str):
        return math.floor(float(number))
