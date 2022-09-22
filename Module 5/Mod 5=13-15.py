import re


def find_all_emails(text):
    result = re.findall(r"[^ 0123456789]\S+\@\w+\.\w{2,}", text)
    print(result)
    return result

print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'))