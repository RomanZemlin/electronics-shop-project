"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src import item


@pytest.fixture
def item1():
    return item.Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return item.Item("Ноутбук", 20000, 5)


def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item1.calculate_total_price() is not None
    assert item2.calculate_total_price() == 100000
    assert item2.calculate_total_price() is not None


def test_apply_discount(item1, item2):
    item1.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0
    assert item1.apply_discount() is not None
    assert item2.apply_discount() == 20000
    assert item2.apply_discount() is not None
