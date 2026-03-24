def f(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    s = [0, 1]
    while len(s) < n:
        s.append(s[-1] + s[-2])
    return s


if __name__ == "__main__":
    print(f(10))
