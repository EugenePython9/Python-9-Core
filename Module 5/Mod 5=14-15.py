import re


def find_all_phones(text):
    result = re.findall(r"[+]380[(]\d\d[)]\d\d\d[-]\d[0-9-]{2}\d\d", text)
    return result