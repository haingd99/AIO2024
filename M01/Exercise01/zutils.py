'''
This lib containt all the share functions support to main program.
The private functions will be built on seperate program.
'''

from math import exp, sqrt
import math

from numpy import random
import sys


def precision(tp,fp):
    return tp / (tp + fp)

def recall(tp, fn):
    return tp / (tp + fn)

def f1_score(precision,recall):
    return 2 * (precision * recall) / (precision + recall)


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
        int_val = int(input)
        if int_val <= 0:
            return 0 # input is an integer <= 0
        else:
            return -1 # input is an integer > 0
    except ValueError as ve:
        try:
            float_val = float(input)            
            return 1 # input is a float
        except ValueError as e:
            return 2 # input is not a digitnum  
        

def sigmoid(x):
    return 1 / (1 + exp(-x))

def relu(x):
    return x if x > 0 else 0 

def elu(x, alpha=1.0):
    return x if x>0 else alpha * (exp(x) - 1)

def MAE(n):
    if numval(n)!=-1:
        print(f"n must be an integer or positive number.")
        sys.exit()

    targets = []
    y_hats = []
    losses = 0
    for i in range(n):
        target = random.uniform(0,10)
        y_hat = random.uniform(0,10)
        targets.append(target)
        y_hats.append(y_hat)
        loss = abs(target - y_hat) / n
        losses += loss
    return y_hats, targets, losses

def MSE(n):
    if numval(n)!=-1:
        print(f"n must be an integer or positive number.")
        sys.exit()

    targets = []
    y_hats = []
    losses = 0

    for i in range(n):
        target = random.uniform(0, 10)
        y_hat = random.uniform(0, 10)
        targets.append(target)
        y_hats.append(y_hat)
        loss = (target - y_hat) ** 2 / n
        losses += loss

    return y_hats, targets, losses

def RMSE(n):
    if numval(n)!=-1:
        print(f"n must be an integer or positive number.")
        sys.exit()

    targets = []
    y_hats = []
    losses = 0

    for i in range(n):
        target = random.uniform(0,10)
        y_hat = random.uniform(0,10)
        targets.append(target)
        y_hats.append(y_hat)
        loss = (target - y_hat) **2 / n
        losses =+ loss
    return y_hats, targets, sqrt(losses)

def ABE(y, y_hat): # Absolute error
    return abs(y - y_hat)


def SQE(y, y_hat): # Square error
    return (y - y_hat) ** 2


def factorial(n):
    """
    Calculate the factorial of n, n is an integer
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def sin(n,x=3.14):
    s = 0
    if numval(n) == -1:
        for i in range(int(n)):
            coe = (-1) ** i
            num = x ** (2 * i + 1)
            dem = factorial(2 * i + 1)
            term = coe * (num / dem)
            s += term
        return s
    else:
        print(f"{n} is not an integer.")   

def cos(x, n):
    s = 0
    if numval(n) == -1:
        for i in range(int(n)):
            coe = (-1) ** i
            num = x ** (2 * i)
            dem = factorial(2 * i)
            term = coe * (num / dem)
            s += term

        return s
    else:
        print(f"{n} is not an integer or non-negative number.")
        sys.exit()

def sinh(x,n):
    s=0
    if numval(n)==-1:
        for i in range(int(n)):
            num = x ** (2 * i + 1)
            dem = factorial(2 * i + 1)
            term = num / dem
            s += term
        return s
    else:
        print(f"{n} is not an integer.")   


def cosh(x,n):
    s=0
    if numval(n)==-1:
        for i in range(int(n)):
            num = x ** (2 * i)
            dem = factorial(2 * i)
            term = num / dem
            s += term
        return s
    else:
        print(f"{n} is not an integer.")   


def MDNRE(y,y_hat,n=2,p=1):
    """
    Calculate Mean Difference and Root Error
    input:
        y: target
        y_hat: predict
        m: number of iterations
        n: n_th root        
        p: degree of los function
    """
    y_root_n = y ** (1 / n)
    y_hat_root_n = y_hat ** (1 / n)
    loss = (y_root_n - y_hat_root_n) ** p
    return loss

def is_number(n):
    try:
        float(n)
        return True
    except ValueError as ve:
        return False


def calc_activation_func(x, act_name):
    if act_name == "relu":
        return relu(x)
    elif act_name == "sigmoid":
        return sigmoid(x)
    elif act_name == "elu":
        return elu(x)
