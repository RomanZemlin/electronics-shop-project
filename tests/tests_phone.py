from src.phone import Phone


iphone = Phone("Iphone", 10000, 20, 1)
samsung = Phone("Samsung", 20000, 5, 2)


def test_repr():
    assert iphone.__repr__() == "Phone('Iphone', 10000, 20, 1)"
    assert samsung.__repr__() == "Phone('Samsung', 20000, 5, 2)"


def test_srt():
    assert iphone.__str__() == "Iphone"
    assert samsung.__str__() == "Samsung"


def test_add():
    assert iphone + samsung == 25
    assert  iphone + iphone == 40


def test_number_of_sim():
    assert iphone.number_of_sim == 1
    assert samsung.number_of_sim == 2


def test_raad():
    assert iphone + samsung == 25
    assert iphone + iphone == 40
