# Calculate the logarithm of a number
import math

def calculate_logarithm(number, base):
    """
    Calculates the logarithm of a number to a specified base.

    Args:
        number (float): The number to calculate the logarithm of.
        base (float): The base of the logarithm.

    Returns:
        float: The logarithm of the number to the specified base.
    """
    return math.log(number,base)
print(calculate_logarithm(8,2))