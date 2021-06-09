import calculator


class testCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(2, 3)

    def test_subtract(self):
        assert 5 == calculator.add(10, 5)
