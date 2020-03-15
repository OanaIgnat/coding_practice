def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n: int) -> int:
    fibs = [1, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]


def fib3(n: int) -> int:
    prev = 1
    fib_ = 1
    for i in range(2, n + 1):
        temp = fib_
        fib_ += prev
        prev = temp
    return fib_


def fib4(n: int) -> int:
    prev = 1
    fib_ = 1
    for i in range(2, n + 1):
        fib_ += prev
        prev = fib_ - prev
    return fib_


def main() -> None:
    for i in range(100):
        print(i, fib4(i))





if __name__ == '__main__':
    main()
