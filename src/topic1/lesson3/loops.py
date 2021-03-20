import numpy as np

if __name__ == '__main__':
    """
    There are two types of loops in Python, for and while.
    
    @see https: // docs.python.org / 3.8 / tutorial / controlflow.html
    4.2. for Statements
    4.3. The range() Function
    4.4. break and continue Statements, and else Clauses on Loops
    4.5. pass Statements¶
    """

    # M1 = [[1,2,3,4,6,10,12],
    #     [5,-6,7,8],
    #     [5,6,5,8],
    #     [1,6,7,11]]
    M2 = [[-1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
    # TODO print diagonal - 1,-6,5,11
    tmp = reversed(M2)
    print(tmp)#.diagonal(M2, offset=0, axis1=0, axis2=1))
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
    result = []
    count = 0
    while (count < 500):
        result.append(count)
        count += 1
    return result


def loops_task2():
    task2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    Use loop for creation new list with even elements [2,4,6,8,10]
    """
    for result in task2:
        if result % 2 == 0:
            return result


