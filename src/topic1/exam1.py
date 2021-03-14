# Листинг 1
# вводим N

# создаем пустой список для хранения простых чисел
n = 100
lst = []
k = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
print(lst)


def loops_exam1():
    """
    Collect all prime numbers in range - 1 to 100

    Prime numbers are numbers that have only 2 factors: 1 and themselves.
    For example, the first 5 prime numbers are 2, 3, 5, 7, and 11.
    By contrast, numbers with more than 2 factors are call composite numbers.

    Here are the first few prime numbers:
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
    61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
    137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, etc.
    """
    n = 50
    lst = [1]
    k = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0

    return lst
