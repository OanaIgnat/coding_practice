"""
Time complexity:
Best: O(n + k)
Avg: O(n + k)
Worst: O(n + k)

Space complexity:
Worst: O(k) k - # elems in frequency list = max element in the array_to_sort
"""


def countingsort(array_to_sort):
    # get max value in the array
    max_val = max(array_to_sort)

    list_sorted = []

    list_counts = [0 for _ in range(0, max_val + 1)]

    # get list of frequencies of each element in array_to_sort
    for i in range(0, len(array_to_sort)):
        list_counts[array_to_sort[i]] += 1

    # add elements in sorted order based on frequency
    for i in range(0, max_val + 1):
        while list_counts[i] > 0:
            list_sorted.append(i)
            list_counts[i] -= 1  # an element can appear multiple times

    return list_sorted


if __name__ == "__main__":
    array = [12, 4, 5, 6, 6, 7, 3, 1, 15]
    print(countingsort(array))
