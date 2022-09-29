import shutil


def create_backup(path, file_name, employee_residence):
    pass

    with open(path + '/' + file_name, 'wb') as opened_file:
        for key, value in employee_residence.items():
            opened_file.write(f'{key} {value}\n'.encode())
        archive_name = shutil.make_archive('backup_folder', 'zip', path)
        return archive_name



# for shortcut, description in shutil.get_archive_formats():
#     print('{:<10} | {:<10}'.format(shortcut, description))


    