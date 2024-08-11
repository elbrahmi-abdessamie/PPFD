import sys

def whatis():
    '''
    Prints if the given command line argument is odd or even
    '''
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) < 2:
        raise AssertionError("no argument is provided")
    else:
        try:
            val = int(sys.argv[1])
            print("I'm Odd." if val%2 else "I'm Even.")
        except:
            raise AssertionError('argument is not an integer')
try:
    whatis()
    print(whatis.__doc__)
except AssertionError as e:
    print("AssertionError:", e)