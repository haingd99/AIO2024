from zutils import SQE,ABE, factorial, MDNRE, is_number, sigmoid, relu, elu, calc_activation_func
from zutils import cos, sin, cosh, sinh


import math
# print(factorial(3))
# def approx_sin(x, terms=10):
#     """
#     Approximate sine of x using the Taylor series expansion.
    
#     Parameters:
#     x (float): The value to calculate the sine of (in radians).
#     terms (int): The number of terms to use in the Taylor series expansion.
    
#     Returns:
#     float: The approximate sine of x.
#     """
#     sine_approx = 0
#     for n in range(terms):
#         coefficient = (-1)**n
#         numerator = x**(2*n + 1)
#         denominator = math.factorial(2*n + 1)
#         term = coefficient * (numerator / denominator)
#         sine_approx += term
    
#     return sine_approx

# # Example usage
# x = math.pi / 10  # 30 degrees in radians
# print(f"Approximate sin({x}): {approx_sin(x)}")
# print(f"Actual sin({x}): {math.cos(x)}")

# print(math.cos(math.pi/10))


# print(MDNRE(0.6,0.1))

# assert is_number(3) == 1
# assert is_number('-2a') == 0.0
# print(is_number(1))
# print(is_number('n'))

# print(is_number(3))
# print(round(sigmoid(3), 2))
# assert round(sigmoid(3), 2) == 0.95
# print(round(sigmoid(2), 2))



# assert round(elu(1,1)) == 1
# print(round(elu(-1,0.01), 2))

# assert calc_activation_func(x = 1.0,act_name='relu') == 1
# print(round(calc_activation_func(x = 3.0, act_name='sigmoid'), 2))


# assert round(sigmoid(3),2)==0.95
# print(round(sigmoid(2),2))


# y = 1
# y_hat = 6
# assert ABE(y, y_hat)==5
# y = 2
# y_hat = 9
# print(ABE(y, y_hat))


# assert SQE(4, 2) == 4
# print(SQE(2, 1))

# assert round(cos(x=1, n=10), 2) ==0.54
# print(round(cos(x=3.14, n=10), 2))


# assert round(sin(x=1, n=10), 4) ==0.8415
# print(round(sin(x=3.14, n=10), 4))
# assert round(sinh(x=1, n=10), 2) ==1.18
# print(round(sinh(x=3.14, n=10), 2))
assert round(cosh(x=1, n=10), 2) ==1.54
print(round(cosh(x=3.14, n=10), 2))                            