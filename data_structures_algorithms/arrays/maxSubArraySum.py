#Find the sum of all possible pairs in an array of N elements
# Input: arr[] = {1, 2}
# Output: 12
# All valid pairs are (1, 1), (1, 2), (2, 1) and (2, 2).
# 1 + 1 + 1 + 2 + 2 + 1 + 2 + 2 = 12

# observe that each elem appears exactly n*n times
def all_pairs_sum(arr):
  return 2 * len(arr) * sum(arr)


# Largest Sum Contiguous Subarray
def maxSubArraySum(arr):
  max_sum = 0
  max_so_far = 0

  for el in arr:
    max_sum += el
    if max_sum > 0:
      if max_so_far < max_sum:
        max_so_far = max_sum
    else:
      max_sum = 0
  return max_so_far


if __name__ == "__main__":
  # print(all_pairs_sum([1,2]))


  # Driver function to check the above function  
  a = [2, -3, 4, -1, -2, 1, 5, -3] 
  print(maxSubArraySum(a))
