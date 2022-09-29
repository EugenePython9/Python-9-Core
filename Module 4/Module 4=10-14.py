from random import randint


def get_random_password():
    random_num = ''
    for i in range(8):
        random_num += chr(randint(40,126))

    return random_num
        

    
    
    
    
        
            
        
            
        
            
    
        
    