import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    ## Tests expected to pass:
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_add_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_subtract_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(0, self.calc.subtract(2, 2))
        self.assertEqual(4, self.calc.subtract(2, -2))
        self.assertEqual(-4, self.calc.subtract(-2, 2))
        self.assertEqual(1, self.calc.subtract(1, 0))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_divide_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_power_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(27, self.calc.power(3, 3))
        self.assertEqual(1, self.calc.power(1, 2))
        self.assertEqual(1, self.calc.power(1, 0))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_square_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(2, self.calc.square(4))
        self.assertEqual(3, self.calc.square(9))
        self.assertEqual(1, self.calc.square(1))
        self.assertEqual(0, self.calc.square(0))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_log10_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(0, self.calc.log10(1))
        self.assertAlmostEqual(0.6020599913279624, self.calc.log10(4))

    ## Tests expected to fail:
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_subtract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.subtract, "2", 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, "2")
        self.assertRaises(TypeError, self.calc.subtract, "2", "2")
        self.assertRaises(TypeError, self.calc.subtract, 1, None)
        self.assertRaises(TypeError, self.calc.subtract, None, 2)
        self.assertRaises(TypeError, self.calc.subtract, object(), 1)
        self.assertRaises(TypeError, self.calc.subtract, 2, object())

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, 1, None)
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, object(), 1)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, 2, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 2, -0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 0, 0)

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, "0", 0)

    def test_square_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.square, "2")
        self.assertRaises(TypeError, self.calc.square, None)
        self.assertRaises(TypeError, self.calc.square, object())

    def test_square_method_fails_with_negative_parameter(self):
        self.assertRaises(ValueError, self.calc.square, -2)
        self.assertRaises(ValueError, self.calc.square, -1)

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "2")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())

    def test_log10_method_fails_with_negative_parameter(self):
        self.assertRaises(ValueError, self.calc.log10, -2)
        self.assertRaises(ValueError, self.calc.log10, -1)

    def test_user_has_no_permissions(self):
        self.calc.user = "user2"
        self.assertRaises(Exception, self.calc.add, 2, 2)
        self.assertRaises(Exception, self.calc.subtract, 2, 2)
        self.assertRaises(Exception, self.calc.multiply, 2, 2)
        self.assertRaises(Exception, self.calc.divide, 2, 2)
        self.assertRaises(Exception, self.calc.power, 2, 2)
        self.assertRaises(Exception, self.calc.square, 2)
        self.assertRaises(Exception, self.calc.log10, 2)



if __name__ == "__main__":  # pragma: no cover
    unittest.main()
