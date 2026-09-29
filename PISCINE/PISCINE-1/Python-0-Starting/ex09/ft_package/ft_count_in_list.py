def count_in_list(lst: list, value) -> int:
    tot = 0
    for i in lst:
        if i == value:
            tot += 1
    return tot
