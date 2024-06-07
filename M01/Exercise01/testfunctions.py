from utils import factorial

print(factorial(3))

import math

def approx_sin(x, terms=10):
    """
    Approximate sine of x using the Taylor series expansion.
    
    Parameters:
    x (float): The value to calculate the sine of (in radians).
    terms (int): The number of terms to use in the Taylor series expansion.
    
    Returns:
    float: The approximate sine of x.
    """
    sine_approx = 0
    for n in range(terms):
        coefficient = (-1)**n
        numerator = x**(2*n + 1)
        denominator = math.factorial(2*n + 1)
        term = coefficient * (numerator / denominator)
        sine_approx += term
    
    return sine_approx

# Example usage
x = math.pi / 10  # 30 degrees in radians
print(f"Approximate sin({x}): {approx_sin(x)}")
print(f"Actual sin({x}): {math.cos(x)}")

print(math.cos(math.pi/10))