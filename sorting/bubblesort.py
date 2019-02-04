"""
Time complexity:
Best: O(n)
Avg: O(n ^ 2)
Worst: O(n ^ 2)

Space complexity:
Worst: O(1) # the array_to_sort is sorted in place
"""


def bubblesort(array_to_sort):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(array_to_sort) - 1):
            if array_to_sort[i] > array_to_sort[i + 1]:
                aux = array_to_sort[i]
                array_to_sort[i] = array_to_sort[i + 1]
                array_to_sort[i + 1] = aux
                sorted = False

    return  array_to_sort



if __name__ == "__main__":
    array = [12, 4, 5, 6, 6, 7, 3, 1, 10]
    print(bubblesort(array))
