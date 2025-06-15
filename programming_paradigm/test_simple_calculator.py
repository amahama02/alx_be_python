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

    # --- Les noms et signatures des méthodes de test sont des correspondances exactes comme demandé. ---

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

    def test_multiplication(self):
        """Test the 'multiply' method with various numbers, including positives, negatives, and zeros."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(1, 1), 1)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_division(self):
        """
        Test the 'divide' method with various valid inputs and crucial edge cases like division by zero.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0)      # Normal division
        self.assertEqual(self.calc.divide(5, 2), 2.5)       # Division avec résultat décimal
        self.assertEqual(self.calc.divide(-10, 2), -5.0)    # Division avec résultat négatif
        self.assertEqual(self.calc.divide(0, 5), 0.0)       # Zéro divisé par un nombre non nul
        self.assertEqual(self.calc.divide(7, 7), 1.0)       # Division par lui-même

        # Test du cas limite critique : division par zéro
        self.assertIsNone(self.calc.divide(5, 0))    # Assure qu'il retourne None lors de la division d'un positif par zéro
        self.assertIsNone(self.calc.divide(0, 0))    # Test 0 divisé par 0 (devrait aussi être None selon la spécification)
        self.assertIsNone(self.calc.divide(-10, 0))  # Test négatif divisé par zéro

# Ce bloc standard permet d'exécuter les tests directement depuis la ligne de commande.
if __name__ == '__main__':
    unittest.main()