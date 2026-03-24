def f(a, b):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


if __name__ == "__main__":
    print(f(48, 18))
