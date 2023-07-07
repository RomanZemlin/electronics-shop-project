from src.keyboard import Keyboard
import pytest


keyboard = Keyboard('Razer', 10000, 55)


def test_srt():
    assert keyboard.__str__() == 'Razer'


def test_language():
    assert keyboard.language == 'EN'
    keyboard.language = 'RU'
    assert keyboard.language != 'EN'
    assert keyboard.language == 'RU'
    with pytest.raises(AttributeError):
        keyboard.language = 'CZ'


def test_change_lang():
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
    keyboard.change_lang().change_lang()
    assert keyboard.language != 'RU'
