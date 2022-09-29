def get_cats_info(path):      
    cat_list = []
    with open (path, 'r') as opened_file:
        while True:
            line = opened_file.readline()
            if not line:
                break
            elif line[-1] == '\n':
                line = line[:-1]            
                
            
            cat_line = line.split(',')
            cat_list.append({'id':cat_line[0], 'name':cat_line[1], 'age':cat_line[2]})
    return cat_list

            