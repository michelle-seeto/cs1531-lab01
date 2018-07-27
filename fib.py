'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''

    fl = []
    n1 = 0;
    n2 = 1;

    for i in range(0,n):                
        n = n1 + n2
        if i >= 1:
            n1 = n2;
            n2 = n
        fl.append(n)

    return fl

if __name__ == '__main__':
    import doctest
    doctest.testmod()
