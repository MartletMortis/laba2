from random import randint

n = int(input("Enter the number of elements in one row/column: "))
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = randint(-10, 10)


def print_matrix(a):
    for j in range(len(a)):
        for i in range(len(a[j])):
            print(a[i][j])
        print()


print_matrix(matrix)


def sum_col(matrix: list):
    return [sum(a) if sum(a) == sum([abs(i) for i in a]) else 'Nothing' for a in matrix]


print(sum_col(matrix))