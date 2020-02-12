"""
Time complexity:
Best: O(1)
Avg: O(log n)
Worst: O(log n)

Space complexity:
Worst: O(1)
"""


def binarysearch(array_to_search, target):
    lower, upper = 0, len(array_to_search) - 1

    while lower <= upper:
        mid = (lower + upper) / 2
        if array_to_search[mid] < target:
            lower = mid + 1
        elif array_to_search[mid] > target:
            upper = mid - 1
        else:
            return mid
    return None # couldn't find it



if __name__ == "__main__":
    array = [12, 4, 5, 6, 7, 3, 1, 15]
    print(binarysearch(sorted(array), 10))
