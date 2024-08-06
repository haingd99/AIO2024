import numpy as np
import pandas as pd


def compute_mean(x):
    t = 0
    for n in x:
        t+=n 
    return t/len(x)


def compute_median(X) :
    size = len(X)
    X = np.sort(X)

    if size % 2 != 0:
        print(X[size//2])
    else :
        print((X[size//2 - 1] + X[size//2]) / 2)


def compute_var(X):
    n=len(X)
    miu = compute_mean(X)
    s = 0 
    for e in X:
        s += (e - miu) ** 2
    return  s / n


def compute_std(X):
    return np.sqrt(compute_var(X))


def compute_covariable(X,Y):
    mean_X = compute_mean(X)
    mean_Y = compute_mean(Y)
    N = len(X)
    cov_X = 0
    cov_Y = 0

    for i in range(N):
        cov_X += X[i] - mean_X
        cov_Y += Y[i] - mean_Y

    return (cov_X * cov_Y) / N


def compute_correlation_cofficient (X, Y):
    '''
    This function calculation correlation coeffiction follow:
    - input: X, Y --> List
    - Output: corr coeff 
                    N*SUM(XY) - SUM(X)*SUM(Y)
        --------------------------------------------------------
        SQRT( (N*SQR(X*Y) - SUM(X)**2) * (N*SQR(X*Y) - SUM(Y)**2)
    '''
    N = len(X)
    numerator = 0
    denominator = 0 
    
    # Cal numerator elements
    n_sum_X = sum(X)
    n_sum_Y = sum(Y)
    n_sum_XY = sum(x*y for x, y in zip(X,Y))

    numerator = (N * n_sum_XY) - (n_sum_X * n_sum_Y)

    # Cal denominator elements
    d_sum_sqr_X = sum(x**2 for x in X)
    d_sum_sqr_Y = sum(y**2 for y in Y)

    denominator = np.sqrt((N * d_sum_sqr_X - n_sum_X ** 2) * (N*d_sum_sqr_Y - n_sum_Y ** 2))

    return np.round(numerator / denominator, 2)

