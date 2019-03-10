'''
Facebook:
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

Note:

1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
If no solution is possible, return an empty list.

'''

'''
Loop i = 1 to N :
    Loop j = i + 1 to N :
        calculate sum
        If in hash table any index already exist for sum then 
            try to find out that it is valid solution or not IF Yes Then update solution
        update hash table
    EndLoop;
EndLoop;

'''


class Solution:
    # @param A : list of integers
    # @return a list of integers

    def equal(self, A):
        dic = {}
        list_res = []
        for a in range(len(A) - 1):
            for b in range(a + 1, len(A)):
                sum = A[a] + A[b]
                if sum in dic:
                    for [c, d] in dic[sum]:
                        if a < c < d and b != d and b != c:
                            list_res.append([a, b, c, d])
                            break
                        if c < a < b and d != b and d != a:
                            list_res.append([c, d, a, b])
                            break
                else:
                    dic[sum] = []

                dic[sum].append([a, b])

        if list_res:
            # sort lexicographic
            list_res.sort(key=lambda x: x[0:4])
            return list_res[0]

        return []


def test_equal():
    s = Solution()
    assert (Solution.equal(s, [1, 1, 1, 1, 1]) == [0, 1, 2, 3])
    assert (Solution.equal(s, [3, 4, 7, 1, 2, 9, 8]) == [0, 2, 3, 5])
    assert (Solution.equal(s, [4, 7, 1, 2, 9]) == [0, 1, 3, 4])


if __name__ == "__main__":
    test_equal()
