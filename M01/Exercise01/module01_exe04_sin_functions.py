import sys
from utils import numval, sin, cos, sinh, cosh


if __name__=="__main__":
    func_list=["sin", "cos", "sinh", "cosh"]
    func=input("Select the function (sin|cos|sinh|cosh):")

    if func.lower() not in func_list:
        print(f"{func} is not supported.")
        sys.exit()

    n=input("Input n:")
    if numval(n)==-1:
        if func.lower()=="sin":
            print(f"{func}({n}): {sin(int(n))}")
        elif func.lower()=="cos":
            print(f"{func}({n}): {cos(int(n))}")
        elif func.lower()=="sinh":
            print(f"{func}({n}): {sinh(int(n))}")
        elif func.lower()=="cosh":
            print(f"{func}({n}): {cosh(int(n))}")