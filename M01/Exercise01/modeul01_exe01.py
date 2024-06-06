'''
• Precision = TP/(TP + FP)
• Recall = TP/(TP + FN)
• F1-score = 2 ∗ (Precision ∗ Recall)/(Precision + Recall)
• Input: function nhận 3 giá trị tp, fp, fn
• Output: print ra kết quả của Precision, Recall, và F1-score
'''

import sys
from utils  import validate, precision, recall, f1_score

if __name__=="__main__":
  
    tp=input("Input True Positive:")
    if validate(tp)>=1: 
        print(f"True Positive must be integer.")        
        sys.exit()
    elif validate(tp)==0: 
        print(f"True Positive must be greater than zero.")        
        sys.exit()

    fp=input("Input False Positive:")
    if validate(fp)>=1:
        print(f"False Positive must be integer.")        
        sys.exit()
    elif validate(fp)==0:
        print(f"False Positive must be greater than zero.")        
        sys.exit()
    
    fn=input("Input False Negative:")
    if validate(fn)>=1:
        print(f"False Negative must be integer.")        
        sys.exit()
    elif validate(fn)==0:
        print(f"False Negative must be greater than zero.")        
        sys.exit()

    pre=precision(int(tp),int(fp))
    rec=recall(int(tp),int(fn)) 
    print(f"Precision: {pre}")
    print(f"Recall: {rec}")
    print(f"F1 score: {f1_score(precision=pre,recall=rec)}")
