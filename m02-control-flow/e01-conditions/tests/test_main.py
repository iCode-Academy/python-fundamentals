import sys
sys.path.insert(0, '..')
from main import grade_score, fizzbuzz


class TestGradeScore:
    def test_grade_a(self):
        assert grade_score(95) == "A"
        assert grade_score(90) == "A"

    def test_grade_b(self):
        assert grade_score(85) == "B"

    def test_grade_c(self):
        assert grade_score(75) == "C"

    def test_grade_d(self):
        assert grade_score(65) == "D"

    def test_grade_f(self):
        assert grade_score(50) == "F"


class TestFizzBuzz:
    def test_fizzbuzz(self):
        assert fizzbuzz(15) == "FizzBuzz"

    def test_fizz(self):
        assert fizzbuzz(9) == "Fizz"

    def test_buzz(self):
        assert fizzbuzz(10) == "Buzz"

    def test_number(self):
        assert fizzbuzz(7) == "7"
