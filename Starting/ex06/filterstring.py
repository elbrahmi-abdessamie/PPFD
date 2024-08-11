from ft_filter import ft_filter
import sys

def process_arguments() -> list:
    '''
    Validate command line args then shape them to the required format
    
    Returns: the new formated list arguments
    '''
    if (lambda x : x == 2)(len(sys.argv) - 1):
        argv =  sys.argv[1:]
    else:
        raise AssertionError("number of typed arguments wrong! <program_name> arg1 arg2")
    try:
        argv[1] = int(argv[1])
    except:
        raise AssertionError("wrong arguments type")
    type_check = lambda x, typ: type(x) is typ
    if type_check(argv[0], str):
        argv[0] = argv[0].split()
        return argv
    else:
        raise AssertionError("wrong arguments type")


def main():
    try:
        args = process_arguments()
        
        print(ft_filter(lambda x: len(x) > args[1], args[0]))
    except AssertionError as e:
        print('AssertionError:', e)

if __name__ == '__main__':
    main()