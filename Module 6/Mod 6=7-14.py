import re
def sanitize_file(source, output):
    with open(source, 'r') as opened_file:
        lines = opened_file.readlines()        
        out = []
        map = {ord('0'): '',ord('1'): '',ord('2'): '',ord('3'): '',ord('4'): '',ord('5'): '',ord('6'): '',ord('7'): '',ord('8'): '',ord('9'): ''}
        for item in lines:
            out.append(item.translate(map))
                  

         
    with open(output, 'w') as opened_file:        
        for item in out:
            opened_file.write(item)

sanitize_file('Text_input.txt', 'Text_output.txt')