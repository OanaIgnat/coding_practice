import random


def random_distr(l):
    r = random.uniform(0, 1)
    print(r)
    s = 0
    for item, prob in enumerate(l):
        s += prob # cumulative distribution
        print(s)
        if s >= r:
            return item
    return item  # Might occur because of floating point inaccuracies

if __name__=="__main__":
    l = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
    print(random_distr(l))