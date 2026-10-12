def check_matrix(mat):
    if len(mat) == 0:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError

def transpose(mat: list[list[float | int]]) -> list[list]:
    check_matrix(mat)
    if len(mat) == 0:
        return []
    res = []
    for i in range(len(mat[0])):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        res.append(new_row)
    return res

def row_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    m = []
    for i in mat:
        s = 0
        for j in i:
            s += j
        m.append(s)
    return m

def col_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    m = []
    for i in range(len(mat[0])):
        s = 0
        for j in range(len(mat)):
            s += mat[j][i]
        m.append(s)
    return m

a = [[[1, 2, 3]],
    [[1], [2], [3]],
    [[1, 2], [3, 4]],
    [],
    [[1, 2], [3]]]
for i in a:
    try:
        print(f'{i} -> {transpose(i)}')
    except ValueError:
        print(f'{i} -> ValueError')

b = [[[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]]
for i in b:
    try:
        print(f'{i} -> {row_sums(i)}')
    except ValueError:
        print(f'{i} -> ValueError')

c = [[[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]]
for i in c:
    try:
        print(f'{i} -> {col_sums(i)}')
    except ValueError:
        print(f'{i} -> ValueError')