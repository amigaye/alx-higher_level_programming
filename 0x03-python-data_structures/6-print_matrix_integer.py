def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print(row[i], end="")
            else:
                print(row[i], end=" ")
        print()
