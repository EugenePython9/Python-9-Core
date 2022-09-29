def save_credentials_users(path, users_info):
    with open(path, 'wb') as opened_file:
        for key, value in users_info.items():
            opened_file.write(f'{key}:{value}\n'.encode())

save_credentials_users('test.txt', {'andry':'uyro18890D', 'steve':'oppjM13LL9e'})