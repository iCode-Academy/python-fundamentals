import sys
sys.path.insert(0, '..')
from main import add_numbers, concat_strings, is_even


class TestAddNumbers:
    def test_positive_numbers(self):
        assert add_numbers(3, 5) == 8

    def test_negative_numbers(self):
        assert add_numbers(-3, -5) == -8

    def test_zero(self):
        assert add_numbers(0, 0) == 0


class TestConcatStrings:
    def test_basic_concat(self):
        assert concat_strings("Hello", "World") == "Hello World"

    def test_empty_first(self):
        assert concat_strings("", "World") == " World"


class TestIsEven:
    def test_even_number(self):
        assert is_even(4) == True

    def test_odd_number(self):
        assert is_even(7) == False

    def test_zero(self):
        assert is_even(0) == True
