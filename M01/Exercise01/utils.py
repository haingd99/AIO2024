def precision(tp,fp):
    return tp/(tp+fp)

def recall(tp, fn):
    return tp/(tp+fn)

def f1_score(precision,recall):
    return 2*(precision*recall)/(precision+recall)


def validate(input):
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
        

def sigmoid():
    pass

def relu():
    pass

def elu(): pass