import calculator


class TestCalculator:
    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_substract(self):
        assert 10 == calculator.substract(20, 10)

    def test_multiply(self):
        assert 5 == calculator.multiply(3, 5)
