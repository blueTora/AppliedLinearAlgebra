import numpy as np

nm = input().split()
n = int(nm[0])
m = int(nm[1])

s = input().split()
p = list(map(float, s))
matrix_A = p

for i in range(n - 1):
    i = i + 1
    s = input().split()
    p = list(map(float, s))
    matrix_A = np.vstack((matrix_A, p))

s = input().split()
p = list(map(int, s))
matrix_B = p

for i in range(m - 1):
    i = i + 1
    s = input().split()
    p = list(map(int, s))
    matrix_B = np.vstack((matrix_B, p))

# matrix_A = [[2, -1, -2],
#             [-4, 6, 3],
#             [-4, -2, 8]]
#
# matrix_B = [[1], [1], [1]]
#
# m = 1
# n = 3

lower = np.zeros((n, n))
upper = np.zeros((n, n))


def calculateLU(u, l):
    length = len(u)

    for i in range(length):
        if i > 0:
            for j in range(i, length):
                for k in range(i, length):
                    u[k][j] -= (u[k][i - 1] / u[i - 1][i - 1]) * u[i - 1][j]

        for ii in range(i, length):
            l[ii][i] = u[ii][i] / u[i][i]

        for j in range(i):
            u[i][j] = 0

    # print('L =')
    # print(l)
    # print()
    # print('U =')
    # print(u)
    # print()


upper = matrix_A
calculateLU(upper, lower)


def forwardSubstitution(a, b):
    x = np.zeros((len(a), 1))

    for i in range(len(a)):

        sum = b[i][0]
        for j in range(i):
            sum -= a[i][j] * x[j][0]

        x[i][0] = sum / a[i][i]

    return x


def backwardSubstitution(a, b):
    x = np.zeros((len(a), 1))
    iter1 = np.arange(len(a))

    for i in -1 - iter1:

        sum = b[i][0]
        iter2 = np.arange(-1 * i)

        for j in -1 - iter2:
            sum -= a[i][j] * x[j][0]

        x[i][0] = sum / a[i][i]

    return x


np.set_printoptions(2)

for entry in range(m):
    b = np.reshape(matrix_B[entry], (n, 1))
    y = forwardSubstitution(lower, b)
    x = backwardSubstitution(upper, y)

    for k in range(n):
        temp = np.round(x[k][0], 2)
        # noinspection PyInterpreter
        print(temp, end=" ")

    print()
