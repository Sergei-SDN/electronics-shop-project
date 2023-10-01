"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item, InstantiateCSVError,CSVError
import os
import pytest
@pytest.fixture()
def item2():
    return Item("Ноутбук", 20000, 5)

def test_calculate_total_price(item2):
    assert item2.calculate_total_price() == 20000 * 5

def test_apply_discount(item2):
    item2.pay_rate = 0.4
    item2.apply_discount()
    assert item2.price == 0.4 * 20000

def test_name(item2):
    item2.name = 'Смартфон'
    assert item2.name == 'Смартфон'

def test_name_len13(item2):
    item2.name = 'СуперСмартфон'
    assert item2.name == 'СуперСмар'

def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr(item2):
    """
    Тестирует метод repr
    """
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test_str(item2):
    """
    Тестирует метод str
    """
    assert str(item2) == 'Ноутбук'

@pytest.fixture()
def file_name():
    return '../src/item.csv'

def test_empty_csv(file_name):
    """Тестирование пустого файла"""
    with pytest.raises(FileNotFoundError):
        path = os.path.join(os.path.dirname(__file__), '..', file_name)
        Item.instantiate_from_csv(path)


def test_broken_csv(file_name):
    """Тестирование поврежденного файла"""
    with pytest.raises(CSVError):
        path = os.path.join(os.path.dirname(__file__), '..', file_name)
        Item.instantiate_from_csv(path)