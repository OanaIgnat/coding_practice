'''
Facebook, Paypal, Yahoo, MIcrosoft, Linkedln, Amazon, Goldman Sachs:
    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer

    # mine: O(n^2) time
    def maxSubArray_O_n2(self, A):
        if A:
            return 0
        max_sum = A[0]
        for i in range(1, len(A)):
            if A[i] > max_sum:
                max_sum = A[i]

        for i in range(1, len(A) - 1):
            if A[i] > 0:
                if A[i] > max_sum:
                    max_sum = A[i]
                s = A[i]
                for j in range(i + 1, len(A)):
                    s += A[j]
                    if s > max_sum:
                        max_sum = s
                s = A[i]
                for j in range(i - 1, 0, -1):
                    s += A[j]
                    if s > max_sum:
                        max_sum = s
        return max_sum

        # @param A : tuple of integers
        # @return an integer
        # O(n) time !!!!
        # First check if all negatives -> max sum is the largest elem in the array

    def maxSubArray(self, A):
        neg = 0
        for i in A:
            if i < 0:
                neg += 1
        if neg == len(A):
            return max(A)
        else:
            s = 0
            m = 0
            for i in range(0, len(A)):
                s += A[i]
                if s > m:
                    m = s
                if s <= 0:
                    s = 0
            return m


def test_maxSubArray():
    s = Solution()
    assert (Solution.maxSubArray(s, [-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [4, -1, 2, 1])


if __name__ == "__main__":
    test_maxSubArray()
