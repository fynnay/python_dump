from random import randint
def safe_cast(inp,to_type,default=None):
    try:
        return to_type(inp)
    except (ValueError,TypeError):
        return default

def confirm(inpMsg=None,GUI=False):
    if not inpMsg is None:
        msg = inpMsg+" "
    else:
        msg =""
    disp = "{0}{1}".format(msg,"Are you sure you want to continue? [y/n]").encode("utf-8")
    if GUI is True:
        uInp = easygui.ynbox(disp)
        if uInp is True:
            return 1
        elif uInp is False:
            return -1
        else:
            return
    else:
        uInp = raw_input(disp).decode("utf-8")
        if uInp == 'y':
            uInp = True
            return 1
        elif uInp == 'n' or uInp == 'c' or uInp == 'q':
            uInp = False
            return -1
        else:
            return

def authenticate():
    accessGranted = False
    while accessGranted is False:
        n1 = randint(1,10)
        n2 = randint(1,10)
        a = n1+n2
        uInp = raw_input( "What is {0}+{1}? (enter [q] to cancel):\n".format(n1,n2).encode("utf-8") ).decode("utf-8")
        if safe_cast(uInp,str) == "q":
            return -1
        elif safe_cast(uInp,int) == a:
            accessGranted = True
    return

if __name__ == '__main__':
    authenticate()