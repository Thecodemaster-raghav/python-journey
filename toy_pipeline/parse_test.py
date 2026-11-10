# for testing the output
from pipeline import convert_secs, find_silences, count_words, longest_line, rows, find_texts, convert_to_buckets
import pytest

def test_convert_secs():
    assert convert_secs("00:00:01,000") == pytest.approx(1.00)
    assert convert_secs("00:00:03,160") == pytest.approx(3.16)
    assert convert_secs("00:00:05,000") == pytest.approx(5.00)
    assert convert_secs("00:00:05,500") == pytest.approx(5.50)
    assert convert_secs("00:00:07,980") == pytest.approx(7.98)
    assert convert_secs("00:00:20,957") == pytest.approx(20.957)

def test_find_silences():
    assert find_silences([{"start": 3.16, "end": 5.00}, {"start":5.50, "end":7.90}], 0.3) == [(5.00, 5.50)]

def test_count_words():
    assert count_words([{"text":"hey karan, how was your day?"}]) == 6

def test_longest_line():
    assert longest_line(rows)["start"] == 7.98
    assert longest_line(rows[::-1])["start"] == 7.98

def test_find_word():
    result = find_texts(rows, "how")
    assert len(result) == 3
    assert result[0]["start"] == 1.0
    assert result[1]["start"] == 3.16
    assert result[2]["start"] == 5.5

def test_convert_to_buckets():
    result = convert_to_buckets(rows)
    assert len(result) == 20
    assert len(result[("ep1", 5)]) == 1
    assert len(result[("ep1", 3)]) == 2
    assert len(result[("ep1", 7)]) == 2