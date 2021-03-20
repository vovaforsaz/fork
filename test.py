import numpy as np

if __name__ == '__main__':
    M2 = [[-1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
    a = []
    for i in range(len(M2)):
        for j in range(len(M2[i])):
            if i == j:
                a.append(M2[i][j])
    print(a)

    print('=======================')

    M3 = [[1, 2, 3, 4],
          [5, 2, 7, 8],
          [5, 6, 3, 8],
          [1, 6, 7, 4]]
    b = []
    for i in reversed(range(len(M3))):
        for j in reversed(range(len(M3[i]))):
            if i == j:
                b.append(M3[i][j])
    print(b)
    print('=======================')

