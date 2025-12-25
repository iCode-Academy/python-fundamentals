import sys
sys.path.insert(0, '..')
from main import sum_list, find_max, count_vowels


class TestSumList:
    def test_positive_numbers(self):
        assert sum_list([1, 2, 3, 4]) == 10

    def test_single_element(self):
        assert sum_list([5]) == 5

    def test_empty_list(self):
        assert sum_list([]) == 0


class TestFindMax:
    def test_find_max_middle(self):
        assert find_max([3, 7, 2, 9, 1]) == 9

    def test_find_max_first(self):
        assert find_max([10, 5, 3]) == 10

    def test_single_element(self):
        assert find_max([42]) == 42


class TestCountVowels:
    def test_hello_world(self):
        assert count_vowels("hello world") == 3

    def test_no_vowels(self):
        assert count_vowels("xyz") == 0

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5
