'''
This lib containt all the share functions support to main program.
The private functions will be built on seperate program.
'''

from math import exp, sqrt
from numpy import random
import sys


def precision(tp,fp):
    return tp/(tp+fp)

def recall(tp, fn):
    return tp/(tp+fn)

def f1_score(precision,recall):
    return 2*(precision*recall)/(precision+recall)


def numval(input):
    '''
    Function: validate an input is a number and which type of object.
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

def MAE(n):
    if numval(n)!=-1:
        print(f"n must be an integer or positive number.")
        sys.exit()

    targets=[]
    y_hats=[]
    losses=0
    for i in range(n):
        target=random.uniform(0,10)
        y_hat=random.uniform(0,10)
        targets.append(target)
        y_hats.append(y_hat)
        loss=abs(target-y_hat)/n
        losses+=loss
    return y_hats, targets, losses

def MSE(n):
    if numval(n)!=-1:
        print(f"n must be an integer or positive number.")
        sys.exit()
    targets=[]
    y_hats=[]
    losses=0
    for i in range(n):
        target=random.uniform(0,10)
        y_hat=random.uniform(0,10)
        targets.append(target)
        y_hats.append(y_hat)
        loss=(target-y_hat)**2/n
        losses+=loss
    return y_hats, targets, losses

def RMSE(n):
    if numval(n)!=-1:
        print(f"n must be an integer or positive number.")
        sys.exit()
    targets=[]
    y_hats=[]
    losses=0
    for i in range(n):
        target=random.uniform(0,10)
        y_hat=random.uniform(0,10)
        targets.append(target)
        y_hats.append(y_hat)
        loss=(target-y_hat)**2/n
        losses=+loss
    return y_hats, targets, sqrt(losses)


def factorial(n):
    
    if numval(n)==-1:
        if n==0: 
            return 1
        else:
            for i in range(n):
                f*=i
            return f
    else:
        print(f"{n} is not an integer.")


def sin(n,x=3.14):
    if numval(n)==-1:
        for i in range(int(n)):
            s+=x-(-1**i)*x**(2*i+1)/factorial(2*i+1)
        return s
    else:
        print(f"{n} is not an integer.")   

def cos(n,x=3.14):
    s=0
    if numval(n)==-1:
        for i in range(n):
            s+=1-(-1**i)*x**(2*i)/factorial(2*i)
        return s
    else:
        print(f"{n} is not an integer.")   

def sinh(n,x=3.14):
    if numval(n)==-1:
        for i in range(n):
            s+=x+x**(2*i+1)/factorial(2*i+1)
        return s
    else:
        print(f"{n} is not an integer.")   


def cosh(n,x=3.14):
    if numval(n)==-1:
        for i in range(n):
            s+=1+x**(2*i)/factorial(2*i)
        return s
    else:
        print(f"{n} is not an integer.")   