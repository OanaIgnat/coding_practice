'''
A Python3 program to find a maximum  
 product of a triplet in an array of integers  
  
 Function to find a maximum product of a  
 triplet in array of integers of size n 

 careful at negative numbers
 can be done in many ways:
 1. most naive: O(n**3)
 2. O(n) time, O(n) space: for each elem: store in a list the min and max elements before and after it (4 numbers for each elem)
 3 (here). O(n logn) time, O(1) space: sort the array using efficient method and take max (first 3 elems, first2 and last)
 4. O(n) time, O(1) space: scan the array and take: max( the first 3 max elems, minimum, 2nd minimum and the first maximum)  
'''
def maxProduct(arr, n):  
  
    # if size is less than 3, no triplet exists  
    if n < 3: 
        return -1
  
    # Sort the array in ascending order  
    arr.sort() 
  
    # Return the maximum of product of last three elements and product of first two elements and last element
    return max(arr[0] * arr[1] * arr[n - 1],  arr[n - 1] * arr[n - 2] * arr[n - 3])
  
# Driver Code 
if __name__ == "__main__": 
  
    arr = [-10, -3, 5, 6, -20]  
    n = len(arr)  
  
    _max = maxProduct(arr, n)  
  
    if _max == -1:  
        print("No Triplet Exists")  
    else: 
        print("Maximum product is", _max)  
