def lookup_key(data, value):
    ret = []
    for l,val in data.items():
        if val == value:
            ret.append(l)        
    return ret       


print (lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))