# Calculate the exponential value of a number
import math

def calculate_exponential(number):
    """
    Calculates the exponential value of a given number.

    Args:
        number (float): The number.

    Returns:
        float: The exponential value of the number.
    """
    return (math.e)**number
print(calculate_exponential(2))