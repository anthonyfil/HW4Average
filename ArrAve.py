def Ave(x):
    if((type(x) == type([1, 1.1])) and len(x) > 0):
        i = 0
        for e in x:
            if(type(e) == type(1) or type(e) == type(1.1)):
                i += e
            else:
                return "Error"
        return (i*1.0/len(x))
    else:
        return "Error"
    
