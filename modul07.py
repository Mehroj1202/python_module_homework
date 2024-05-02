# Calculate the ceiling and floor values of a number
import math

def calculate_ceiling_floor(number):
    """
    Calculates the ceiling and floor values of a number.

    Args:
        number (float): The number.

    Returns:
        tuple: A tuple containing the ceiling and floor values of the number.
    """
    return math.ceil(number),math.floor(4.3)
print(calculate_ceiling_floor(4.3))