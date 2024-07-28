import sys

MORSE_CODE_DICT = { ' ':'/ ', 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def arg_validator() -> str:
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        raise AssertionError("the arguments are bad")

def standerlize(string: str):
    string = string.upper()
    return string

def encrypt(string: str) -> str:
    cipher = ''
    string_to_encode = standerlize(string)
    validator = lambda x : x.isalnum() or x.isspace()
    for char in string_to_encode:
        if not validator(char):
            raise AssertionError("the arguments are bad")
        cipher += ' ' + MORSE_CODE_DICT[char]
    return cipher

def main():
    try:
        string_to_encode = arg_validator()
        encoded_str = encrypt(string_to_encode)
        print(encoded_str)
    except AssertionError as msg:
        print('AssertionError:', msg)
        
if __name__ == '__main__':
    main()