"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src import item
from src.item import Item

item1 = item.Item("Смартфон", 10000, 20)
item2 = item.Item("Ноутбук", 20000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1.pay_rate = 0.8
    assert item1.price * item1.pay_rate == 8000.0
    assert item2.price == 20000


def test_name():
    assert item1.name == "Смартфон"
    assert item2.name == "Ноутбук"


def test_name_setter():
    assert len(item1.name) <= 10
    assert len(item2.name) <= 10


def test_normal_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 7


def test_string_to_number():
    assert item1.string_to_number("9.8") == 9
    assert item2.string_to_number("11.4") == 11
