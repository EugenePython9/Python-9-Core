def formatted_numbers():
    formatted_list = ['|{:^10}|{:^10}|{:^10}|'.format('decimal','hex','binary')]
    for i in range (16):
        formatted_list.append('|{:<10d}|{:^10x}|{:>10b}|'.format(i,i,i)) 
        


    return formatted_list
    
        
for el in formatted_numbers():
    print(el)