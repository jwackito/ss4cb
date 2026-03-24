def f(lst, t):
    i = 0
    while i < len(lst):
        if lst[i] == t:
            return i
        i += 1
    return -1


if __name__ == "__main__":
    print(f([34, 7, 23, 32, 5, 62, 14, 89], 32))
