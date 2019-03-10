'''
Google:
    Add One To Number:
    Given a non-negative number represented as an array of digits,
    add 1 to the number ( increment the number represented by the digits ).
    The digits are stored such that the most significant digit is at the head of the list.
    Example:
    If the vector has [1, 2, 3]
    the returned vector should be [1, 2, 4]
    as 123 + 1 = 124.

    OBS!!!
    [0, 2\ -> [3]
    [0,2,0,1] -> [0, 2, 0, 2]
    [9 , 9] -> [1, 0, 0]
    [0, 9, 9] -> [1, 0, 0]
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers


    def plusOne(self, A):
        if len(A) == 1:
            if A[0] < 9:
                return [A[0] + 1]
            else:
                return [1, 0]
        j = len(A) - 1
        while A[j] == 9:
            A[j] = 0
            j -= 1
        if j == -1:
            return [1] + A
        elif j == 0:
            return [A[j] + 1] + A[j + 1:]
        else:
            while 1:
                if A[0] == 0:
                    A.pop(0)
                    j -= 1
                else:
                    break
            return A[0:j] + [A[j] + 1] + A[j + 1:]


def test_plusOne():
    s = Solution()
    assert (Solution.plusOne(s, [0, 1]) == [2])
    assert (Solution.plusOne(s, [0]) == [1])
    assert (Solution.plusOne(s, [9]) == [1, 0])
    assert (Solution.plusOne(s, [0, 9, 9]) == [1, 0, 0])
    assert (Solution.plusOne(s, [0, 2, 3]) == [2, 4])
    assert (Solution.plusOne(s, [1, 2, 9]) == [1, 3, 0])
    assert (Solution.plusOne(s, [9, 9]) == [1, 0, 0])


if __name__ == "__main__":
    test_plusOne()
