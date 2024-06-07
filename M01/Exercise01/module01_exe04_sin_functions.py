import sys
from utils import numval, sin, cos, sinh, cosh


if __name__=="__main__":
    func_list=["sin", "cos", "sinh", "cosh"]
    func=input("Select the function (sin|cos|sinh|cosh):")

    if func.lower() not in func_list:
        print(f"{func} is not supported.")
        sys.exit()

    x=input("Input x:")
    n=input("Input n:")
    
    if (numval(n)==-1) and (numval(x)==1):
        if func.lower()=="sin":
            print(f"{func}({x}), {n}: {round(sin(float(x),int(n)),2)}")
        elif func.lower()=="cos":
            print(f"{func}({x}), {n}: {round(cos(float(x),int(n)),2)}")
        elif func.lower()=="sinh":
            print(f"{func}({x}), {n}: {round(sinh(float(x),int(n)),2)}")
        elif func.lower()=="cosh":
            print(f"{func}({x}, {n}): {round(cosh(float(x),int(n)),2)}")
