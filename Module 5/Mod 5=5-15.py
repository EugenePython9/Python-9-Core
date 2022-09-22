def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    phone_dict = {
    "UA": [],
    "JP": [],
    "TW": [],
    "SG": []
}
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        if phone.startswith('81'):
            #phone_dict.update({'JP':phone_dict['JP'].append(phone)})
            phone_dict['JP'].append(phone)
        elif phone.startswith('65'):
            #phone_dict.update({'SG':phone_dict['SG'].append(phone)})
            phone_dict['SG'].append(phone)
        elif phone.startswith('886'):
            #phone_dict.update({'TW':phone_dict['TW'].append(phone)})
            phone_dict['TW'].append(phone)
        else:
            #phone_dict.update({'UA':phone_dict['UA'].append(phone)})
            phone_dict['UA'].append(phone)
    return phone_dict



# def get_phone_numbers_for_countries(list_phones):
#     JP = []
#     SG = []
#     TW = []
#     UA = []
#     for phone in list_phones:
#         phone = sanitize_phone_number(phone)
#         if phone.startswith('81'):
#             JP.append(phone)
#         elif phone.startswith('65'):
#             SG.append(phone)
#         elif phone.startswith('886'):
#             TW.append(phone)
#         else:
#             UA.append(phone)
#     phone_dict = {
#     "UA": UA,
#     "JP": JP,
#     "TW": TW,
#     "SG": SG
# }
#     return phone_dict



print(get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976']))




