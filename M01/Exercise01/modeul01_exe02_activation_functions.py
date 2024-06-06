from utils import sigmoid, relu, elu, validate
import sys 

if __name__=="__main__":
    funcs_list = ["sigmoid", "relu", "elu"]
    func=input("Input activation Function (sigmoid|relu|elu):")
    
    if str.lower(func) not in funcs_list: 
        print(f"{func} is not supported.")
        sys.exit()
    else:
        x=input("Input x value:")
        if validate(x)==2:
            print(f"{x} is not a number.")
            sys.exit()
        if func.lower()=="elu":
            alpha=input(f"Input alpha for {func}:")
            if validate(alpha)==2:
                print(f"Alpha must be a number.")
                sys.exit()
            else:
                e=elu(alpha=float(alpha),x=float(x))
                print(f"{func} result is: {e}")
        else: 
            print(f"{func} result is: {relu(float(x))}")
            print(f"{func} result is: {sigmoid(float(x))}")


    

