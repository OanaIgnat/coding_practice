
def largest_subarray_sum0(arr):
  d = {}
  max_len = 0
  max_len_elem = []
  sum_elem = 0
  
  for i in range(len(arr)):
    sum_elem += arr[i]
    if sum_elem in d.keys():
      # there is a zero sum
      len_zero_sum = i - d[sum_elem]
      if len_zero_sum > max_len:
        max_len = len_zero_sum         
        max_len_elem = arr[d[sum_elem]:max_len + d[sum_elem] + 1]
    else:
      d[sum_elem] = i
  return max_len, max_len_elem


# @param arr: tuple of integers [2, 7, 11, 15]
# @param a : integer 9
# @return a list of integers
def twoSum(arr, a):
  d={}
  for el in arr:
    res = a - el
    if res not in d:
      d[res] = el
    if el not in d:
      d[el] = res
    else:
      return [res, el]    


def threeSum(arr, a):
  for i in range(len(arr)-1):
    el = a - arr[i]
    next_elems = twoSum(arr[i+1: ], el)
    if next_elems:
      return ([arr[i]] + next_elems)


if __name__ == "__main__":
  # arr = [15, -2, 2, -8, 1, 7, 10 ,23]
  # max_len, max_len_elem = largest_subarray_sum0(arr)
  # print(max_len)
  # print(max_len_elem)
  # print(twoSum([15, -2, 2, -8, 1, 7, 10 ,23], 0))
  print(threeSum([15, -2, 2, -8, 1, 7, 10 ,23], 7))
