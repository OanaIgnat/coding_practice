class Solution:
    def tribonacci1(self, n: int) -> int:
        if n is 0:
            return 0
        elif n is 1 or n is 2:
            return 1
        else:
            # exponential time complexity: 3 ** n -> out of memory
            return self.tribonacci(n - 2) + self.tribonacci(n - 1) + self.tribonacci(n)

    def tribonacci2(self, n: int) -> int:
        # O(n) space complexity
        tribs = [0, 1, 1]
        for i in range(3, n):
            tribs.append(tribs[i - 1] + tribs[i - 2] + tribs[i - 3])
        return tribs[n]

    def tribonacci3(self, n: int) -> int:

        # O(n) time complexity, constant space complexity
        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for i in range(n - 2):
            x, y, z = y, z, x + y + z
        return z


def tribonacci4(self, n: int) -> int:
    n = 38
    nums = [0] * n
    nums[1] = nums[2] = 1
    for i in range(3, n):
        nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]

    return nums[n]
