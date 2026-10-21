# fucntion for testing the code before pushing it to the production server
from pay import calc_pay
from decimal import Decimal

def test_calc_pay():
    assert calc_pay(10, Decimal("20.00"), 20, False) == Decimal("210.00")

def test_calc_pay2():
    assert calc_pay(10, Decimal("20.00"), 30, True) == Decimal("307.50")