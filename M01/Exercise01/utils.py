from math import exp
def precision(tp,fp):
    return tp/(tp+fp)

def recall(tp, fn):
    return tp/(tp+fn)

def f1_score(precision,recall):
    return 2*(precision*recall)/(precision+recall)


def validate(input):
    '''
    input: input
    output:
    - 0: integer negative
    - (-1): integer positive
    - 1: float
    - 2: string or not a digit
    '''
    try:
        int_val=int(input)
        if int_val<=0:
            return 0 # input is an integer < 0
        else:
            return -1
    except ValueError as ve:
        try:
            float_val=float(input)            
            return 1 # input is a float
        except ValueError as e:
            return 2 # input is not a digitnum  
        

def sigmoid(x):
    return 1/(1+exp(x))

def relu(x):
    return x if x>0 else 0 

def elu(alpha,x):
    return x if x>0 else alpha*(exp(x)-1)