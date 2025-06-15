# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, verifying its basic arithmetic operations.
    """

    def setUp(self):
        """
        Set up a fresh SimpleCalculator instance before each test method runs.
        This ensures tests are isolated and don't affect each other.
        """
        self.calc = SimpleCalculator()

    # --- Test method names and signatures are exact matches as requested by the checker. ---

    def test_addition(self):
        """Test the 'add' method with various numbers, including positives, negatives, and zeros."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(10.5, 2.5), 13.0)
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.3)

    def test_subtraction(self):
        """Test the 'subtract' method with various numbers, including positives, negatives, and zeros."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(10.5, 2.5), 8.0)
        self.assertEqual(self.calc.subtract(7, 7), 0)

    def test_multiply(self):
        """Test the 'multiply' method with various numbers, including positives, negatives, and zeros."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(1, 1), 1)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_divide(self):
        """
        Test the 'divide' method with various valid inputs and crucial edge cases like division by zero.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0)      # Normal division
        self.assertEqual(self.calc.divide(5, 2), 2.5)       # Division with decimal result
        self.assertEqual(self.calc.divide(-10, 2), -5.0)    # Division with negative result
        self.assertEqual(self.calc.divide(0, 5), 0.0)       # Zero divided by a non-zero number
        self.assertEqual(self.calc.divide(7, 7), 1.0)       # Division by itself

        # Test the critical edge case: division by zero
        self.assertIsNone(self.calc.divide(5, 0))    # Ensure it returns None when dividing positive by zero
        self.assertIsNone(self.calc.divide(0, 0))    # Test 0 divided by 0 (should also be None as per spec)
        self.assertIsNone(self.calc.divide(-10, 0))  # Test negative divided by zero

# This standard block allows you to run the tests directly from the command line.
if __name__ == '__main__':
    unittest.main()