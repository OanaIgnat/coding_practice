'''
Facebook:
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]

Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer

'''


class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange_my_sol_not_optimum(self, A):
        n = len(A)
        if n % 10 == 0:
            power_ten = n // 10
        else:
            power_ten = n // 10 + 1
        for i in range(0, n):
            A[i] = A[A[i]] % (10 ** power_ten) * (10 ** power_ten) + A[i] % (10 ** power_ten)

        for i in range(0, n):
            A[i] = A[i] // (10 ** power_ten)

    '''
    
    Now, we will do a slight trick to encode 2 numbers in one index. 
    This trick assumes that N * N does not overflow.
    Given a number as
       A = B + C * N   if ( B, C < N )
       A % N = B
       A / N = C
    '''

    def arrange(self, A):
        n = len(A)
        for i in range(0, n):
            A[i] = A[A[i]] % n * n + A[i] % n

        for i in range(0, n):
            A[i] = A[i] // n


def test_arrange():
    s = Solution()
    assert (Solution.arrange(s, [1, 0]) == [0, 1])
    assert (Solution.arrange(s, [2, 0, 1]) == [1, 2, 0])
    assert (Solution.arrange(s, [1, 2, 7, 0, 9, 3, 6, 8, 5, 4, 11, 10]) == [2, 7, 8, 1, 4, 0, 6, 5, 3, 9, 10, 11])


if __name__ == "__main__":
    test_arrange()
