from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    
    for i in path.iterdir(): 
        if i.is_dir():
            folders.append(i.name)
        elif i.is_file():
            files.append(i.name)
                    
    return files, folders


path = Path('C:\PYTHON')
print (parse_folder(path))