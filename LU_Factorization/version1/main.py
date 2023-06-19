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


def calculateLU(mat):

    for i in range(n):

        for k in range(i, n):

            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            upper[i][k] = mat[i][k] - sum

        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])

    # print('L =')
    # print(l)
    # print()
    # print('U =')
    # print(u)
    # print()


calculateLU(matrix_A)


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
        print(temp, end=" ")

    print()
