"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # merge sort -> O(n log n) time complexity & O(n) space complexity

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged

    def merge_sorted_arrays_extra_space(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        nums = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while j < n:
            nums.append(nums2[j])
            j += 1

        while i < m:
            nums.append(nums1[i])
            i += 1

        print(nums)

    def merge_sorted_arrays_in_place(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        if not nums2:
            return nums1
        if not nums1:
            return nums2

        while i < m:
            if nums1[i] > nums2[j]:
                temp = nums1[i]
                nums1[i] = nums2[j]
                nums2[j] = temp
                nums2.sort()
            i += 1

        while j < n:
            nums1[i] = nums2[j]
            j += 1
            i += 1

        print(nums1)


    # What if we start to overwrite nums1 from the end, where there is no information yet? Then no additional space is needed.
    def merge_sorted_arrays_in_place2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def main():
    s = Solution()
    s.merge_sorted_arrays_in_place([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)


if __name__ == "__main__":
    main()
