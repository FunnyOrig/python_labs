def min_max(nums: list[float | int]) -> tuple[float | int , float | int]:
    if len(nums) == 0:
        raise ValueError
    min_num = nums[0]
    max_num = nums[0]
    for i in nums:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    res = (min_num, max_num)
    return res

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    uniq = []
    for x in nums:
        if x not in uniq: uniq.append(x)
        c = len(uniq)
        for i in range(c):
            for j in range(0, c - i - 1):
                if uniq[j] > uniq[j + 1]:
                    uniq[j], uniq[j + 1] = uniq[j + 1], uniq[j]
    return uniq

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if isinstance(row, (list, tuple)):
            for i in row: result.append(i)
        else: raise TypeError
    return result

a = [[3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [],
    [1.5, 2, 2.0, -3.1]]
for i in a:
    try:
        print(f'{i} -> {min_max(i)}')
    except ValueError:
        print(f'{i} -> ValueError')

b = [[3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0]]
for i in b:
    print(f'{i} -> {unique_sorted(i)}')

c = [[[1, 2], [3, 4]],
    [[1, 2], (3, 4, 5)],
    [[1], [], [2, 3]],
    [[1, 2], "ab"]]
for i in c: 
    try:
        print(f'{i} -> {flatten(i)}')
    except TypeError: print(f'{i} -> TypeError')