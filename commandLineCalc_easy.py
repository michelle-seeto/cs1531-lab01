'''
make a command line calculator

DIFFICULTY = MEDIUM
TOPICS = strings, variables, lists

your task is to write a command line calculator
this task is easy since we can use the eval function to do most of the legwork
however, we need to parse possible invalid user input. This is your task

return None if invalid input. Otherwise return the result
'''

def calculate(s):
    '''
    >>> calculate("1+3")
    4
    >>> calculate("1+3*4/3")
    5.0
    >>> calculate("(1+3)*5")
    20
    >>> calculate("-----1")
    -1
    >>> calculate("-+-1")
    1
    >>> calculate(\'print("bad guy coming to hack")\')
    '''
    
    allowed_ch = ['0','1','2','3','4','5','6','7','8','9','*','+','-','/','(',')']

    for ch in s:
        if allowed_ch.count(ch) == 0:
            result = None
            break
        else:
            result = eval(s)

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
