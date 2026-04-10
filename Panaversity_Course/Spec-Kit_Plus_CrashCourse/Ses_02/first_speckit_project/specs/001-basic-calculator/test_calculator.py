import unittest
from calculator import calculate, parse_expression

class TestCalculate(unittest.TestCase):
    def test_addition(self):
        """Test that addition is calculated correctly."""
        self.assertEqual(calculate(10, '+', 5), 15.0)

    def test_subtraction(self):
        """Test that subtraction is calculated correctly."""
        self.assertEqual(calculate(10, '-', 5), 5.0)

    def test_multiplication(self):
        """Test that multiplication is calculated correctly."""
        self.assertEqual(calculate(10, '*', 5), 50.0)

    def test_division(self):
        """Test that division is calculated correctly."""
        self.assertEqual(calculate(10, '/', 5), 2.0)

    def test_rounding(self):
        """Test that division with rounding is calculated correctly."""
        self.assertEqual(calculate(1, '/', 3), 0.3333)

    def test_divide_by_zero(self):
        """Test that division by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            calculate(10, '/', 0)

class TestParseExpression(unittest.TestCase):
    def test_simple_expression(self):
        """Test that a simple expression is parsed correctly."""
        self.assertEqual(parse_expression("10.5 * 5"), (10.5, '*', 5.0))

    def test_whitespace_handling(self):
        """Test that expressions with extra whitespace are parsed correctly."""
        self.assertEqual(parse_expression("  10.5   *   5  "), (10.5, '*', 5.0))
        self.assertEqual(parse_expression("10 + 5"), (10.0, '+', 5.0))
        self.assertEqual(parse_expression("  10 - 5   "), (10.0, '-', 5.0))

    def test_invalid_expressions(self):
        """Test that invalid expressions raise a ValueError."""
        with self.assertRaises(ValueError):
            parse_expression("5 * * 5")  # Malformed
        with self.assertRaises(ValueError):
            parse_expression("5 +")      # Incomplete
        with self.assertRaises(ValueError):
            parse_expression("a + 5")    # Non-numeric operand
        with self.assertRaises(ValueError):
            parse_expression("")         # Empty string
        with self.assertRaises(ValueError):
            parse_expression("   ")      # Whitespace-only string


if __name__ == '__main__':
    unittest.main()
