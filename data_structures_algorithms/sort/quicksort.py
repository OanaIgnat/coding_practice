"""
Time complexity:
Best: O(n log n)
Avg: O(n log n)
Worst: O(n ^ 2)

Space complexity:
Worst: O(n log n)
"""


def quicksort(array_to_sort):
    less = []
    equal = []
    greater = []

    # take into account when list has only one element or 0
    if len(array_to_sort) > 1:
        pivot = array_to_sort[0]
        for x in array_to_sort:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array_to_sort


if __name__ == "__main__":
    array = [12, 4, 5, 6, 7, 3, 1, 15]
    print(quicksort(array))
