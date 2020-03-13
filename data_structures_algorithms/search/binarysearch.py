"""
Time complexity:
Best: O(1)
Avg: O(log n)
Worst: O(log n)

Space complexity:
Worst: O(1)

Cool Facts:
If you are setting mid = (left + right) / 2, you have to be very careful.
Unless you are using a language that does not overflow such as Python, left + rightleft+right could overflow.
One way to fix this is to use left + (right - left) / 2 instead.

If you fall into this subtle overflow bug, you are not alone.
Even Jon Bentley's own implementation of binary search had this overflow bug and remained undetected for over twenty years.
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
    return None  # couldn't find it


"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version == 5:  # some chosen version
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower, upper = 1, n

        while lower <= upper:
            mid = (lower + upper) // 2
            if not isBadVersion(mid):
                lower = mid + 1
            else:
                upper = mid - 1
                if not isBadVersion(upper):
                    return mid
        return None


if __name__ == "__main__":
    array = [12, 4, 5, 6, 7, 3, 1, 15]
    print(binarysearch(sorted(array), 10))
