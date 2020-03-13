#Find the sum of all possible pairs in an array of N elements
# Input: arr[] = {1, 2}
# Output: 12
# All valid pairs are (1, 1), (1, 2), (2, 1) and (2, 2).
# 1 + 1 + 1 + 2 + 2 + 1 + 2 + 2 = 12

# observe that each elem appears exactly n*n times
def all_pairs_sum(arr):
  return 2 * len(arr) * sum(arr)


# Largest Sum Contiguous Subarray
def maxSubArraySum(nums):
  max_sum = nums[0]

  for i in range(1, len(nums)):
    if nums[i - 1] > 0:
      nums[i] += nums[i - 1]
    max_sum = max(nums[i], max_sum)
  return max_sum





if __name__ == "__main__":
  # print(all_pairs_sum([1,2]))


  # Driver function to check the above function  
  a = [2, -3, 4, -1, -2, 1, 5, -3] 
  print(maxSubArraySum(a))
