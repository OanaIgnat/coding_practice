# O(log n)
def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1.0 / power(x, -n)
    elif n == 1:
        return x
    else:
        if n % 2 == 0:
            return power(x * x, n // 2)
        else:
            return power(x * x, n // 2) * x


def main():
    print(power(2, 6))
    print(power(2, 5))


if __name__ == "__main__":
    main()
