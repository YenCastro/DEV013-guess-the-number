import unittest
from main import random_number, get_user_guess, get_computer_guess, check_guess
from unittest.mock import patch

class TestGuessGame(unittest.TestCase):
    """Clase de pruebas unitarias para guess the number"""

    def setUp(self):
        """Configuración inicial para las pruebas"""
        self.secret_number = 42
        self.valid_input = '50'
        self.invalid_input = ['abc', '101', '50']

    def test_random_number(self):
        """Número secreto entre 1 y 100"""
        secret_number = random_number()
        self.assertTrue(1 <= secret_number <= 100)

    def test_user_guess_valid_input(self):
        """Prueba de la función userGuess con una entrada válida"""
        with patch('builtins.input', return_value=self.valid_input):
            user_input = get_user_guess()
        self.assertEqual(user_input, int(self.valid_input))

    def test_user_guess_invalid_input(self):
        """Prueba de la función userGuess con entradas inválidas"""
        with patch('builtins.input', side_effect=self.invalid_input):
            with patch('builtins.print') as mock_print:
                user_input = get_user_guess()
                mock_print.assert_called_with("Oh, try again! Please enter a number between 1 and 100")
        self.assertEqual(user_input, 50)

    def test_get_computer_guess(self):
        """Número secreto entre 1 y 100"""
        comp_guess_number = get_computer_guess()
        self.assertTrue(1 <= comp_guess_number <= 100)

    def test_check_guess(self):
        """Probamos que la función check_guess devuelva los resultados esperados"""
        self.assertEqual(check_guess(1, self.secret_number),
                         (False, "Ups! It seems the number is higher, keep trying."))
        self.assertEqual(check_guess(42, self.secret_number),
                         (True, "Congratulations! The number entered is correct."))
        self.assertEqual(check_guess(89, self.secret_number),
                         (False, "Ups! It seems the number is lower, keep trying."))

if __name__ == '__main__':
    unittest.main()