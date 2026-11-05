# for testing the output
from pipeline import convert_secs
import pytest

def test_convert_secs():
    assert convert_secs("00:00:01,000") == pytest.approx(1.00)
    assert convert_secs("00:00:03,160") == pytest.approx(3.16)
    assert convert_secs("00:00:05,000") == pytest.approx(5.00)
    assert convert_secs("00:00:05,500") == pytest.approx(5.50)
    assert convert_secs("00:00:07,980") == pytest.approx(7.98)
    assert convert_secs("00:00:20,957") == pytest.approx(20.957)