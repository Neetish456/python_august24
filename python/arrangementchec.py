def arrangement(string1):
    open , close = 0
    arrangement1 = True 
    for char in string1:
        if char == '(':
            open += 1
        else:
            close += 1
        if close> open:
            arrangement1 = False
            break
    
