def real_len(text):
    length = 0
    for char in text:       
        if char in  ['\n', '\f', '\r', '\t', '\v']:
             continue       
        
        length += 1
        
    return length
    
print (real_len('Alex\nKdfe23\t\f\v.\r'))