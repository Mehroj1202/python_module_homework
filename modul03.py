# Perform trigonometric calculations
from math import sin,cos

def perform_trigonometric_calculations(angle):
    """
    Performs trigonometric calculations for a given angle in degrees.

    Args:
        angle (float): The angle in degrees.

    Returns:
        tuple: A tuple containing the sine, cosine, and tangent of the angle.
    """
    return sin(angle),cos(angle),sin(angle)/cos(angle),cos(angle)/sin(angle)
print(perform_trigonometric_calculations(45))