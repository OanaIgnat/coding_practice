'''
Google:
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if not A:
            return []
        if max(A) < 0:
            return []

        s = 0
        max_s = 0
        max_elems = []
        elems = []
        for i in range(0, len(A)):
            if A[i] >= 0:
                s += A[i]
                elems += [A[i]]
            else:
                if max_s < s:
                    max_s = s
                    max_elems = elems
                if max_s == s:
                    if len(max_elems) < len(elems):
                        max_s = s
                        max_elems = elems
                s = 0
                elems = []
            if max_s < s:
                max_s = s
                max_elems = elems
        return max_elems


def test_maxset():
    s = Solution()
    assert (Solution.maxset(s, [1, 2, 5, -7, 2, 3]) == [1, 2, 5])
    assert (Solution.maxset(s, []) == [])
    assert (Solution.maxset(s, [756898537, -1973594324, -2038664370, -184803526, 1424268980]) == [1424268980])
    assert (Solution.maxset(s, [756898537, -1973594324, -2038664370, 184803526, 1424268980]) == [184803526, 1424268980])


if __name__ == "__main__":
    test_maxset()
