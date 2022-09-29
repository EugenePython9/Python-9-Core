def is_equal_string(utf8_string, utf16_string):       
    s_from_utf16 = utf16_string.decode('utf-16')
    s_from_utf8 = utf8_string.decode()
    s_from_utf8.casefold()
    s_from_utf16.casefold()
    if s_from_utf16 == s_from_utf8:
        return True
    else:
        return False