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
    target=random.uniform(0,len(n))
    y_hat=random.uniform(0,len(n))
    losses=[]
    for i in range(len(n)):
        loss=abs(target[i]-y_hat[i])/n
        losses.append(loss)
    return losses

def MSE(n):
    if numval(n)!=-1:
        print(f"n must be an integer or positive number.")
        sys.exit()
    target=random.uniform(0,len(n))
    y_hat=random.uniform(0,len(n))
    losses=[]
    for i in range(len(n)):
        loss=(target[i]-y_hat[i])**2/n
        losses.append(loss)
    return losses

def RMSE(n):
    if numval(n)!=-1:
        print(f"n must be an integer or positive number.")
        sys.exit()
    target=random.uniform(0,len(n))
    y_hat=random.uniform(0,len(n))
    losses=[]
    for i in range(len(n)):
        loss=sqrt((target[i]-y_hat[i])**2/n)
        losses.append(loss)
    return losses