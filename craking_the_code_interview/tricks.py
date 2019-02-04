from functools import reduce


def map_filter_reduce():
    items = [1, 2, 3, 4]
    squared = list(map(lambda x: x ** 2, items))
    [x ** 2 for x in items]
    less_than_2 = list(filter(lambda x: x < 2, items))
    [x for x in items if x < 2]
    product = reduce((lambda x, y: x * y), items)
    sum(x for x in items)
    return squared, less_than_2, product


def main():
    items = [1, 2, 3, 4, 1, 2]
    duplicates = set([x for x in items if items.count(x) > 1])

    x1 = {1, 2, 3}
    x2 = {2, 4, 5}
  #   x1 - x2 = {1, 3}
  #   x2 - x1 = x2.difference(x1) =  {4, 5}
  #   x2.intersection(x1) = {2}


if __name__ == "__main__":
    main()
