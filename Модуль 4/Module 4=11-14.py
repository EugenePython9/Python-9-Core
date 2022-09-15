def is_valid_password(password):
    if type(password) != str:
        return False
    elif len(password) < 8:
        return False

    numbers = '1234567890'
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = 0 ; a = 0 ; A = 0
    for letter in password:
        if letter in numbers:
            n += 1
        elif letter in alphabet:
            a += 1
        elif letter in Alphabet:
            A += 1
    
    if n and a and A:
        return True
    else:
        return False


