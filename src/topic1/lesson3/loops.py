"""Examples of using loops.

The original module unconditionally imported :mod:`numpy` at import time
even though the library is only required for demonstration code inside the
``__main__`` section.  The execution environment used for the kata does not
include ``numpy`` which caused ``ModuleNotFoundError`` during test discovery
when importing this module.  To keep the training exercises lightweight and
free of unnecessary dependencies we avoid importing ``numpy`` unless the
demonstration block is executed directly.
"""

from typing import List

if __name__ == '__main__':
    # Import numpy only for the interactive examples below.  This avoids a
    # hard dependency on numpy when the module is imported elsewhere (e.g. in
    # the unit tests).
    import numpy as np

    """
    There are two types of loops in Python, for and while.

    @see https: // docs.python.org / 3.8 / tutorial / controlflow.html
    4.2. for Statements
    4.3. The range() Function
    4.4. break and continue Statements, and else Clauses on Loops
    4.5. pass Statements¶
    """
    M2 = [[-1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
    # TODO print diagonal - 1,-6,5,11
    for i in range(len(M2)):
        for j in reversed(range(len(M2))):
            if i == j:
                print(M2[i][j], end='')
            else:
                print('   ', end='')
        print()
    print('=======================')
    print(np.diagonal(M2, offset=0, axis1=0, axis2=1))


    M2 = [[-1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
    # TODO print diagonal - 1,-6,5,11
    for i in range(len(M2)):
        for j in range(len(M2)):
            if i == j:
                print(M2[i][j], end='')
            else:
                print('   ', end='')
        print()
    print('=======================')
    print(np.diagonal(M2, offset = 0,axis1=0, axis2=1))

    M1 = [[1, 2, 3, 4, 111, 6, 7, 11, 100],
          [5, -6, 7, 8, 11, 8, 11],
          [5, 2, -42, 8, 11],
          [1, 6, 7, 11, 100]]

    for i in range(len(M1)):
        for j in range(len(M1[i])):
            print(M1[i][j])
        print('-----------------------')




    # For loops iterate over a given sequence.
    list_numbers = [2, 4, 6, 8]
    for number in list_numbers:
        print(number)

    # For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
    for n in range(5):
        print("range(5)", n)

    for n in range(3, 5):
        print("range(3, 5)", n)

    # "while" loops
    count = 0
    while count < 5:
        print("while loop ", count)
        count += 1  # This is the same as count = count + 1

    # "break" and "continue" statements
    '''
    break is used to exit a for loop or a while loop,
    Whereas continue is used to skip the current block, and return to the "for" or "while" statement.
    '''
    count = 0
    while True:
        print("count True - ", count)
        if count >= 5: break
        count += 1

    # Unlike languages like C,CPP.. we can use else for loops. When the loop condition of "for" or "while"
    count = 0
    while (count < 5):
        print("count - ", count)
        count += 1
    else:
        print("count value reached %d" % (count))

    arrays = []
    count = 1
    while (count < 501):
        arrays.append(count)
        count += 1
    print(arrays)

    # task2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # for number in task2:
    #     if number %2 == 0:
    #         print(number)

def loops_task1():
    """
    Use loop for creation list with 500 integer elements
    """
    result: List[int] = []
    count = 0
    while count < 500:
        result.append(count)
        count += 1
    return result


def loops_task2():
    task2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """Return a list containing only the even numbers from ``task2``.

    The previous implementation returned only the first even element because it
    exited the loop on the first match.  The function is intended to collect all
    even numbers, so we accumulate them in a list and return it.
    """
    evens: List[int] = []
    for number in task2:
        if number % 2 == 0:
            evens.append(number)
    return evens


