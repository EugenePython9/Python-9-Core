import re

def total_salary(path):
    total = 0
    #try:
    opened_file = open(path, 'r')
    while True:
        line = opened_file.readline()
        if not line:
            break
        salary = re.search('\d+', line)
        total += float(salary.group())

    #finally:
    opened_file.close()

    return total