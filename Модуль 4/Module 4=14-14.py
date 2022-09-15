import sys


def parse_args():
    result = ""
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        result += arg + ' '
     
    return result.rstrip() 