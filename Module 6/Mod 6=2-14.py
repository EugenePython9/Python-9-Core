def write_employees_to_file(employee_list, path):
    opened_file = open (path, 'w')
    for list in employee_list:
        for line in list:
            line += '\n'
            print (line)
            opened_file.write(line)

    opened_file.close()
            
                
    
        