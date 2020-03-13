"""
Time complexity:
Best: O(n log n)
Avg: O(n log n)
Worst: O(n log n)

Space complexity:
Worst:O(n)
"""


def merge_sort(array_to_sort):
    if len(array_to_sort) < 2:
        return array_to_sort

    result = []
    mid = len(array_to_sort) // 2

    left = merge_sort(array_to_sort[:mid])
    right = merge_sort(array_to_sort[mid:])
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    result += left[i:]
    result += right[j:]

    return result


if __name__ == "__main__":
    array = [12, 4, 5, 6, 6, 7, 3, 1, 10]
    print(merge_sort(array))
