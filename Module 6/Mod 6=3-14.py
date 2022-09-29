def read_employees_from_file(path):
    opened_file = open (path, 'r')
    list_of_emploee = []    
    lines = opened_file.readlines()
    for line in lines:
        if line[-1] == '\n':
            list_of_emploee.append(line[:-1])
        else:
            list_of_emploee.append(line)
    
         
    opened_file.close()
    return list_of_emploee  