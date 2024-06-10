import math

# pylint: disable=no-else-return
def convert_to_number(operand):
    try:
        if "." in operand:
            return float(operand)
        else:
            return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def InvalidConvertToNumber(operand):
    try:
        if "." in operand:
            return (float(operand))

        return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")
    return user == "user1"


def check_positive(x):
    try:
        if math.isnan(x):
            x = convert_to_number(x)
    except TypeError:
        raise ValueError("Parameter must be a number")

    if x < 0:
        raise ValueError("Parameter must be a positive number")
