def is_valid_pin_codes(pin_codes):
    if pin_codes  == []:
        print('empty')
        return False
        
    numbers = ('1234567890')
    codelist = set()
    for code in pin_codes:     
        
        if type(code) != str:
            print('not a string')
            return False
        
        elif len(code) != 4:
            print('len != 4')
            return False

        elif code in codelist:
            print('double')
            return False
        
        for i in code:            
            if i not in numbers:
                print('Nan')                
                return False
        codelist.add(code)

        print (codelist, type(code), len(code))
    
    return True

print (is_valid_pin_codes([]))