'''
• Precision = TP/(TP + FP)
• Recall = TP/(TP + FN)
• F1-score = 2 ∗ (Precision ∗ Recall)/(Precision + Recall)
• Input: function nhận 3 giá trị tp, fp, fn
• Output: print ra kết quả của Precision, Recall, và F1-score

NOTE: Đề bài yêu cầu các điều kiện sau
•Phải kiểm tra giá trị nhận vào tp, fp, fn là type int, nếu là type khác thì print ví dụ
check fn là float, print ’fn must be int’ và thoát hàm hoặc dừng chương trình.
•Yêu cầu tp, fp, fn phải đều lớn hơn 0, nếu không thì print ’tp and fp and fn must be
greater than zero’ và thoát hàm hoặc dừng chương trình
'''

import sys
from zutils  import numval, precision, recall, f1_score

if __name__=="__main__":
  
    tp=input("Input True Positive:")
    if numval(tp)>=1: 
        print(f"True Positive must be integer.")        
        sys.exit()
    elif numval(tp)==0: 
        print(f"True Positive must be greater than zero.")        
        sys.exit()

    fp=input("Input False Positive:")
    if numval(fp)>=1:
        print(f"False Positive must be integer.")        
        sys.exit()
    elif numval(fp)==0:
        print(f"False Positive must be greater than zero.")        
        sys.exit()
    
    fn=input("Input False Negative:")
    if numval(fn)>=1:
        print(f"False Negative must be integer.")        
        sys.exit()
    elif numval(fn)==0:
        print(f"False Negative must be greater than zero.")        
        sys.exit()

    pre=precision(int(tp),int(fp))
    rec=recall(int(tp),int(fn))
    f1=f1_score(precision=pre,recall=rec) 

    assert round(f1_score(precision=pre,recall=rec), 2) == 0.33
    print(f"Precision: {round(pre,2)}")
    print(f"Recall: {round(rec,2)}")
    print(f"F1 score: {round(f1,2)}")
