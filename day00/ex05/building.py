import sys

def ispunct(c):
    '''
    Check if the given character is punctualion 

    Args:
        c (str): the character to check
    
    Returns:
        bool: True if it is punctuation otherwise False
    '''
    ascii_code = ord(c)
    if ascii_code in range(33, 47) or ascii_code in range(58, 64):
        return True
    else:
        return False

def counter(string: str) -> dict:
    '''
    Count number of spaces, digits, upper|lower letters and punctualtion chars

    Args:
        string (str): the string to process
    
    Returns:
        dict: string processing result stored in dict 
    '''
    content = {}
    content['upper letters'] = sum(c.isupper() for c in string)
    content['lower letters'] = sum(c.islower() for c in string)
    content['punctuation marks'] = sum(1 for c in string if ispunct(c))
    content['spaces'] = sum(c.isspace() for c in string)
    content['digits'] = sum(c.isdigit() for c in string)
    return content

def get_arg() -> str:
    '''
    Get string we need to process eighter from 
    command argument or from the prompt(stdin)

    Args:
        
    Returns:
        str: extracted string
    '''
    if len(sys.argv) > 2:
        raise AssertionError("more then one argument is provided")
    elif len(sys.argv) == 2:
        return sys.argv[1]
    else:
        return (input("What is the text to count?\n"))

def print_dict(result: dict):
    '''
    Prints dict content as value key

    Args:
        result (dict): dictionary to print
    
    Returns:
    
    '''
    for x in result.keys():
       print(result[x], x, sep=' ')

def main():
    try:
        string = get_arg()
        print(f"The text contains {len(string)} characters:")
        print_dict(counter(string))
    except (AssertionError, EOFError) as e:
        print("AssertionError:", e)
    



if __name__ == '__main__':
    main()  