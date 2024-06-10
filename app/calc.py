import app
import math

import app.util

class InvalidPermissions(Exception):
    pass

class Calculator:
    user : str = "user1"

    def add(self, x, y):
        self.check_permissions(f"{x} + {y}", self.user)
        self.check_types(x, y)
        return x + y

    def subtract(self, x, y):
        self.check_permissions(f"{x} - {y}", self.user)
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        self.check_permissions(f"{x} * {y}", self.user)
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_permissions(f"{x} / {y}", self.user)
        self.check_types(x, y)
        if y == 0:
            raise ZeroDivisionError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_permissions(f"{x} ** {y}", self.user)
        self.check_types(x, y)
        return x ** y

    def square(self, x):
        self.check_permissions(f"sqrt({x})", self.user)
        self.check_types(x, 0)
        app.util.check_positive(x)
        return math.sqrt(x)

    def log10(self, x):
        self.check_permissions(f"log10({x})", self.user)
        self.check_types(x, 0)
        app.util.check_positive(x)
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    def check_permissions(self, operation, user):
        if not app.util.validate_permissions(operation, user):
            raise InvalidPermissions('User has no permissions')



if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.divide(2,10)
    print(result)
