# Calculate the ceiling and floor values of a number
from  math import ceil,floor

def calculate_ceiling_floor(number):
    """
    Calculates the ceiling and floor values of a number.

    Args:
        number (float): The number.

    Returns:
        tuple: A tuple containing the ceiling and floor values of the number.
    """
    return ceil(number),floor(number)
print(calculate_ceiling_floor(3.7))
print(calculate_ceiling_floor(4.3))