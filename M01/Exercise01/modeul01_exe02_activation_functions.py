'''
•Input:
    •Người dùng nhập giá trị x
    •Người dùng nhập tên activation function chỉ có 3 loại (sigmoid, relu, elu)
•Output: Kết quả f(x) (x khi đi qua activation function tương ứng theo activation function
name). Ví dụ nhập x=3, activation_function = ’relu’. Output: print ’relu: f(3)=3’
NOTE: Lưu ý các điều kiện sau:
•Dùng function is_number được cung cấp sẵn để kiểm tra x có hợp lệ hay không (vd:
x=’10’, is_number(x) sẽ trả về True ngược lại là False). Nếu không hợp lệ print ’x must
be a number’ và dừng chương trình.
•Kiểm tra activation function name có hợp lệ hay không nằm trong 3 tên (sigmoid,
relu, elu). Nếu không print ’ten_function_user is not supported’ (vd người dùng
nhập ’belu’ thì print ’belu is not supported’)
•Convert x sang float type
•Thực hiện theo công thức với activation name tương ứng. Print ra kết quả
•Dùng math.e để lấy số e
•α = 0.01
'''

from zutils import sigmoid, relu, elu, numval
import sys 

if __name__=="__main__":
    funcs_list = ["sigmoid", "relu", "elu"]
    func=input("Input activation Function (sigmoid|relu|elu):")
    
    if str.lower(func) not in funcs_list: 
        # Validation the input of activation function. If func is not valid, exit.
        print(f"{func} is not supported.")
        sys.exit()
    else:
        
        x=input("Input x value:")
        if numval(x)==2:
            # validation input of x. If x is not valid, exit.
            print(f"{x} is not a number.")
            sys.exit()

        if (func.lower()=="elu"):
            '''
            if func == elu --> checking x and if x <0 then input alpha --> checking the alpha --> invalid: exit, else calculate elu.
            '''
            if float(x)<0:
                alpha=input(f"Input alpha for {func}:")
                if numval(alpha)==2:
                    # validation input of alpha, alpha must be number. If alpha is not valid, exit.
                    print(f"Alpha must be a number.")
                    sys.exit()
                else:
                    e=elu(alpha=float(alpha),x=float(x))
                    print(f"{func}: f({e})")
            else:
                # x>0 then set alpha==1
                alpha=1
                e=elu(alpha=float(alpha),x=float(x))
                print(f"{func}: f({e})")
        else: 
            if func.lower()=="relu":
                print(f"{func}: f({relu(float(x))})")
            if func.lower()=="sigmoid":
                print(f"{func}: f({sigmoid(float(x))})")


    

