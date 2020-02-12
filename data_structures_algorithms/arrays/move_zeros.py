'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

'''


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        # If the current element is not 0, then we need to
        # append it just in front of last non 0 element we found.
        for i in range(len(nums)):
            if nums[i]:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        # After we have finished processing new elements,
        # all the non-zero elements are already at beginning of array.
        # We just need to fill remaining array with 0's.
        for i in range(lastNonZeroFoundAt, 0, -1):
            nums[i] = 0
