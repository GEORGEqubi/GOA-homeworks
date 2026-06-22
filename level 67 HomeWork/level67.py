def solve(st):
    
    if len(st) % 2 != 0:
        return -1
    
    
    
    start = 0
    stop = 0
    
    for i in st:
        if i == "(":
            start += 1
        else:
            if start > 0:
                start -=1
            else:
                stop += 1
    return (stop + 1) // 2 + (start +1) // 2

