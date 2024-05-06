import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_with_positive_input(self):
        number = 10
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0,1,1,2,3,5,8,13,21,34]

        number = 5
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0,1,1,2,3]

    def test_fibonacci_with_negative_input(self):
        number = -2
        result = fibonacci.get_fibonacci_series(number)
        assert result is None

    def test_fibonacci_with_zero_input(self):
        number = 0
        result = fibonacci.get_fibonacci_series(number)
        assert result == None

    def test_fibonacci_with_one_input(self):
        number = 1
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0]

    def test_fibonacci_with_wrong_input_type(self):
        number = 2.5
        result = fibonacci.get_fibonacci_series(number)
        assert result == None

unittest.main()



