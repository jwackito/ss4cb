def f(lst, t):
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] == t:
            return m
        elif lst[m] < t:
            l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == "__main__":
    print(f([2, 5, 8, 12, 16, 23, 38, 45, 67, 90], 23))
