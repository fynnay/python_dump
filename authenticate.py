'''
File: authenticate.py
Description: Some simple functions, that are often used to ask for user confirmation. For use in Terminal.
'''
from random import randint

def safe_cast(inp, to_type, default=None):
    '''Convert value type without throwing an error.
    '''
    try:
        return to_type(inp)
    except (ValueError, TypeError):
        return default

def userConfirm(inpMsg=None):
    '''Presents a simple yes/no question.
    '''
    if not inpMsg is None:
        msg = inpMsg+" "
    else:
        msg = ""
    disp = "{0}{1}".format(msg, "Are you sure you want to continue? [y/n]").encode("utf-8")
    uInp = raw_input(disp).decode("utf-8")
    if uInp == 'y':
        uInp = True
        return 1
    elif uInp == 'n' or uInp == 'c' or uInp == 'q':
        uInp = False
        return -1
    else:
        return -2

def securityMath():
    '''Presents a simple math problem. The user has to input the correct solution.
    Returns 1 if solution is correct
    Returns -1 if user cancelled
    Returns -2 if solution is incorrect
    '''
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    a = n1+n2
    uInp = raw_input("What is {0}+{1}? (enter [q] to cancel):\n".format(n1, n2).encode("utf-8")).decode("utf-8")
    if safe_cast(uInp, str) == "q":
        return -1
    elif safe_cast(uInp, int) == a:
        return 1
    else:
        return -2

if __name__ == '__main__':
    print userConfirm()
    print securityMath()
