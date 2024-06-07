import sys
from zutils import MDNRE, MAE

if __name__=="__main__":
    y=[100,50,20,5.5,1,0.6]
    y_hat=[99.5,49.5,19.5,5,0.5,0.1]
    for i in range(len(y)):
        print(f"Target: {y[i]} - Predict: {y_hat[i]} - MDNRE: {MDNRE(y[i],y_hat[i])}") 
        