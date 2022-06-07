src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]


def unique_nums(lst):
    unique_lst = set()
    _ = set()
    for num in lst:
        if num not in _:
            unique_lst.add(num)
        else:
            unique_lst.discard(num)
        _.add(num)
    return [num for num in lst if num in unique_lst]



print(unique_nums(src))
