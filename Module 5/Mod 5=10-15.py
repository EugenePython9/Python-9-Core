import re


def find_word(text, word):
    result_dict = {
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': word,
    'string': text
}
    
    stroka = re.search(word, text)
    if stroka:
        x = stroka.span()
        # print (stroka.span(), stroka.group(), stroka.string)
        result_dict['first_index'] = x[0]
        result_dict['last_index'] = x[1]
        result_dict['result'] = True
    return result_dict

print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"))




