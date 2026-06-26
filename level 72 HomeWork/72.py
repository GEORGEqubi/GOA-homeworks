def order(sentence):
    
    words = sentence.split()
    result = []
    if  sentence == "":
        return ""
    
    for i in range(1,10):
        for ss in words:
            if str(i) in ss:
                result.append(ss)
                
    return " ".join(result)

print(order("4of Fo1r pe6ople g3ood th5e the2"))