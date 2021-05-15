from apps import calculator


class TestCalculator:
    def test_add(self):
        assert calculator.add(2, 2) == 4

    def test_substract(self):
        assert calculator.substract(20, 10) == 10

    def test_multiply(self):
        assert calculator.multiply(3, 5) == 15

    def test_divisor(self):
        assert calculator.divisor(24, 12) == 2

    def test_divisor_fail(self):
        assert calculator.divisor(5, 0) is None
