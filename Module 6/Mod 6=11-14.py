def get_credentials_users(path):
    with open(path, 'rb') as opened_file:
        spysok =[]
        while True:
            line = (opened_file.readline()).decode()
            if not line:
                break
            if line[-1] == '\n':
                spysok.append(line[:-1])
            else:
                spysok.append(line)
            #print(spysok)
    return spysok
        
