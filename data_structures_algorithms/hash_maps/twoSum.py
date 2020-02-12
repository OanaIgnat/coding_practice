'''
Facebook, Amazon, Google:
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 0, index2 = 1
'''


class Solution:

    def my_sol_inneficient(self, A, B):
        sol = []

        dict_j = {}
        for j in range(len(A)):
            if A[j] not in dict_j.keys():
                dict_j[A[j]] = []
            dict_j[A[j]].append(j)

        for i in range(len(A)):
            target = B - A[i]
            if target in dict_j.keys():
                for k in range(0, len(dict_j[target])):
                    if i < dict_j[target][k]:
                        sol.append([i + 1, dict_j[target][k] + 1])
                        break

        sol.sort(key=lambda x: x[1])
        if not sol:
            return []
        return sol[0]


    # @param A : tuple of integers [2, 7, 11, 15]
    # @param B : integer 9
    # @return a list of integers
    def twoSum(self, A, B):
        dic = {}
        for i in range(len(A)):
            target = B - A[i] #complement
            if target not in dic:
                if A[i] not in dic:
                    dic[A[i]] = i + 1
            else:
                return [dic[target], i + 1]

        return []


def test_twoSum():
    s = Solution()
    assert (Solution.twoSum(s, [2, 7, 11, 15], 9) == [1, 2])
    assert (Solution.twoSum(s, [1, 1, 1], 2) == [1, 2])


if __name__ == "__main__":
    test_twoSum()
