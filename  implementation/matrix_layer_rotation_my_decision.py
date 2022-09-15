import itertools
from time_execute import time_decorator


def matrixRotation(matrix, x_y):
    list_cache = []
    for i, list_of_matrix in enumerate(matrix[x_y:len(matrix) - x_y]):
        next_elem = matrix[(i + x_y + 1) % len(matrix)]
        if i + x_y == len(matrix) - x_y - 1:
            list_of_matrix.pop(-1 - x_y)
            list_of_matrix.insert(x_y + 0, list_cache[-1])
            # list_cache.pop(0)
        elif i + x_y != x_y + 0:
            first_elem = list_of_matrix.pop(x_y + 0)
            list_of_matrix.pop(-1 - x_y)
            list_of_matrix.insert(x_y + 0, list_cache[-1])
            list_cache.append(first_elem)
            list_of_matrix.insert(len(list_of_matrix) - x_y, next_elem[-1 - x_y])
            # list_cache.pop(0)
        else:
            list_of_matrix.insert(len(list_of_matrix) - x_y, next_elem[-1 - x_y])
            list_cache.append(list_of_matrix.pop(x_y + 0))


# first_multiple_input = [6, 6, 1000000]
first_multiple_input = input().rstrip().split()
m = int(first_multiple_input[0])
n = int(first_multiple_input[1])
r = int(first_multiple_input[2])
matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().rstrip().split())))


@time_decorator
def main():
    for _, i in itertools.product(range(r), range(min(m, n) // 2)):
        matrixRotation(matrix, i)
    for matrix_fi in matrix:
        print(matrix_fi)


if __name__ == '__main__':
    main()
