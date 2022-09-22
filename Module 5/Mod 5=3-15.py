def sanitize_phone_number(phone):
    clear_phone =''
    for i in phone:
        if i in {'1','2','3','4','5','6','7','8','9','0'}:
            clear_phone += i
        else:
            continue
    return clear_phone

