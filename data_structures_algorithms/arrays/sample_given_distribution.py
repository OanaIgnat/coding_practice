import random


def random_distr(l):
    r = random.uniform(0, 1)
    print(r)
    s = 0
    for item, prob in l:
        s += prob  # cumulative distribution
        if s >= r:
            return item
    return item  # Might occur because of floating point inaccuracies


if __name__ == "__main__":
    l = [[0, 0.1], [1, 0.05], [2, 0.05], [3, 0.2], [4, 0.4], [5, 0.2]]
    print(random_distr(l))
