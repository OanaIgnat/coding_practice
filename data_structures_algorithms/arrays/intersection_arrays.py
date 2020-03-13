from typing import List, Set


class Solution:
    def set_intersection(self, set1, set2):
        # To solve the problem in linear time, let's use the structure set,
        # which provides in/contains operation in O(1) time in average case.
        return [x for x in set1 if x in set2]

    # Time complexity : O(n+m), where n and m are arrays' lengths.
    # O(n) time is used to convert nums1 into set, O(m) time is used to convert nums2,
    # and contains/in operations are O(1) in the average case.

    # Space complexity : O(m+n) in the worst case when all elements in the arrays are different.
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1) < len(nums2):
            return self.set_intersection(nums1, nums2)
        else:
            return self.set_intersection(nums2, nums1)

    # what if arrays are sorted?
    # O(n) time complexity & O(1) space (the output is not considered)
    def intersection_sorted(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()

        result = set()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
