def add_employee_to_file(record, path):
    opened_file = open (path, 'a')
    opened_file.write(record + '\n')
    opened_file.close()
    
    
